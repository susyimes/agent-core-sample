# LangMem - Long-Term Memory Enrichment Manager (_MEMORY_INSTRUCTIONS)

Title: LangMem - Long-Term Memory Enrichment Manager (_MEMORY_INSTRUCTIONS)
Source-URL: https://raw.githubusercontent.com/langchain-ai/langmem/main/src/langmem/knowledge/extraction.py
Source-Repo-or-Site: langchain-ai/langmem
Original-Path: src/langmem/knowledge/extraction.py
Category: Memory Systems Deep / Semantic-Episodic Enrichment
Tags: langmem,langgraph,memory-enrichment,semantic-memory,episodic-memory,trustcall
Retrieved: 2026-11-07
Value-Note: LangMem core enrichment doctrine: extract, compare/update, synthesize semantic+procedural+episodic memory with confidence caveats. Distinct from procedural prompt optimizer (05) in same repo.
Truncation-Note: Original is 2114 lines; verbatim lines 1-536 kept (schemas, thread extractor, _MEMORY_INSTRUCTIONS, MemoryManager). Remaining store-manager plumbing omitted; full file at Source-URL.

--- ORIGINAL ---
````python
import asyncio
import datetime
import typing
import uuid

from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage, AnyMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable, RunnableConfig, RunnableLambda
from langchain_core.runnables.config import get_executor_for_config
from langgraph.store.base import (
    NOT_PROVIDED,
    BaseStore,
    NotProvided,
)
from langgraph.store.base import (
    Item as BaseItem,
)
from langgraph.store.base import (
    SearchItem as BaseSearchItem,
)
from langgraph.utils.config import ensure_config, get_store
from pydantic import BaseModel, Field
from trustcall import create_extractor
from typing_extensions import TypedDict

from langmem import utils
from langmem.knowledge.tools import create_search_memory_tool

## LangGraph Tools

# ```python setup
# from langmem import create_memory_store_manager
# from langgraph.store.memory import InMemoryStore
# manager = create_memory_store_manager(
#     "anthropic:claude-3-5-sonnet-latest",
#     namespace=("chat",),
#     store=InMemoryStore(),
# )
# ```  # end-setup


class Item(BaseItem):
    value: BaseModel | dict[str, typing.Any]

    def dict(self) -> dict:
        result = super().dict()
        if isinstance(self.value, BaseModel):
            result["value"] = self.value.model_dump(mode="json")
        return result


class SearchItem(BaseSearchItem):
    value: BaseModel | dict[str, typing.Any]

    def dict(self) -> dict:
        result = super().dict()
        if isinstance(self.value, BaseModel):
            result["value"] = self.value.model_dump(mode="json")
        return result


class MessagesState(TypedDict):
    messages: list[AnyMessage]


class MemoryState(MessagesState):
    existing: typing.NotRequired[list[tuple[str, BaseModel]]]
    max_steps: int  # Default of 1


class SummarizeThread(BaseModel):
    title: str
    summary: str


class ExtractedMemory(typing.NamedTuple):
    id: str
    content: BaseModel


S = typing.TypeVar("S", bound=type)


class Memory(BaseModel):
    """Call this tool once for each new memory you want to record. Use multi-tool calling to record multiple new memories."""

    content: str = Field(
        description="The memory as a well-written, standalone episode/fact/note/preference/etc."
        " Refer to the user's instructions for more information the preferred memory organization."
    )


@typing.overload
def create_thread_extractor(
    model: str,
    /,
    schema: None = None,
    instructions: str = "You are tasked with summarizing the following conversation.",
) -> Runnable[MessagesState, SummarizeThread]: ...


@typing.overload
def create_thread_extractor(
    model: str,
    /,
    schema: S,
    instructions: str = "You are tasked with summarizing the following conversation.",
) -> Runnable[MessagesState, S]: ...


def create_thread_extractor(
    model: str,
    /,
    schema: typing.Union[None, BaseModel, type] = None,
    instructions: str = "You are tasked with summarizing the following conversation.",
) -> Runnable[MessagesState, BaseModel]:
    """Creates a conversation thread summarizer using schema-based extraction.

    This function creates an asynchronous callable that takes conversation messages and produces
    a structured summary based on the provided schema. If no schema is provided, it uses a default
    schema with title and summary fields.

    Args:
        model (str): The chat model to use for summarization (name or instance)
        schema (Optional[Union[BaseModel, type]], optional): Pydantic model for structured output.
            Defaults to a simple summary schema with title and summary fields.
        instructions (str, optional): System prompt template for the summarization task.
            Defaults to a basic summarization instruction.

    Returns:
        extractor (Callable[[list], typing.Awaitable[typing.Any]]): Async callable that takes a list of messages and returns a structured summary

    ???+ example "Examples"
        ```python
        from langmem import create_thread_extractor

        summarizer = create_thread_extractor("gpt-4")

        messages = [
            {"role": "user", "content": "Hi, I'm having trouble with my account"},
            {
                "role": "assistant",
                "content": "I'd be happy to help. What seems to be the issue?",
            },
            {"role": "user", "content": "I can't reset my password"},
        ]

        summary = await summarizer.ainvoke({"messages": messages})
        print(summary.title)
        # Output: "Password Reset Assistance"
        print(summary.summary)
        # Output: "User reported issues with password reset process..."
        ```

    """
    if schema is None:
        schema = SummarizeThread

    extractor = create_extractor(model, tools=[schema], tool_choice="any")

    template = ChatPromptTemplate.from_messages(
        [
            ("system", instructions),
            (
                "user",
                "Call the provided tool based on the conversation below:\n\n<conversation>{conversation}</conversation>",
            ),
        ]
    )

    def merge_messages(input: dict) -> dict:
        conversation = utils.get_conversation(input["messages"])

        return {"conversation": conversation} | {
            k: v for k, v in input.items() if k != "messages"
        }

    return (
        merge_messages | template | extractor | (lambda out: out["responses"][0])
    ).with_config({"run_name": "thread_extractor"})  # type: ignore


_MEMORY_INSTRUCTIONS = """You are a long-term memory manager maintaining a core store of semantic, procedural, and episodic memory. These memories power a life-long learning agent's core predictive model.

What should the agent learn from this interaction about the user, itself, or how it should act? Reflect on the input trajectory and current memories (if any).

1. **Extract & Contextualize**  
   - Identify essential facts, relationships, preferences, reasoning procedures, and context
   - Caveat uncertain or suppositional information with confidence levels (p(x)) and reasoning
   - Quote supporting information when necessary

2. **Compare & Update**  
   - Attend to novel information that deviates from existing memories and expectations.
   - Consolidate and compress redundant memories to maintain information-density; strengthen based on reliability and recency; maximize SNR by avoiding idle words.
   - Remove incorrect or redundant memories while maintaining internal consistency

3. **Synthesize & Reason**  
   - What can you conclude about the user, agent ("I"), or environment using deduction, induction, and abduction?
   - What patterns, relationships, and principles emerge about optimal responses?
   - What generalizations can you make?
   - Qualify conclusions with probabilistic confidence and justification

As the agent, record memory content exactly as you'd want to recall it when predicting how to act or respond. 
Prioritize retention of surprising (pattern deviation) and persistent (frequently reinforced) information, ensuring nothing worth remembering is forgotten and nothing false is remembered. Prefer dense, complete memories over overlapping ones."""


class Done(BaseModel):
    """Only call this tool once you are done forming & consolidating memories.
    Before that, continue to refine existing memories by patching and removing them
    or create new ones."""

    pass


class MemoryManager(Runnable[MemoryState, list[ExtractedMemory]]):
    def __init__(
        self,
        model: str | BaseChatModel,
        *,
        schemas: typing.Sequence[typing.Union[BaseModel, type]] = (Memory,),
        instructions: str = _MEMORY_INSTRUCTIONS,
        enable_inserts: bool = True,
        enable_updates: bool = True,
        enable_deletes: bool = False,
    ):
        self.model = (
            model if isinstance(model, BaseChatModel) else init_chat_model(model)
        )
        self.schemas = schemas or (Memory,)
        self.instructions = instructions
        self.enable_inserts = enable_inserts
        self.enable_updates = enable_updates
        self.enable_deletes = enable_deletes

    async def ainvoke(
        self,
        input: MemoryState,
        config: typing.Optional[RunnableConfig] = None,
        **kwargs: typing.Any,
    ) -> list[ExtractedMemory]:
        max_steps = input.get("max_steps")
        if max_steps is None:
            max_steps = 1
        messages = input["messages"]
        existing = input.get("existing")
        prepared_messages = self._prepare_messages(messages, max_steps)
        prepared_existing = self._prepare_existing(existing)
        # Track external memory IDs (those passed in from outside)
        external_ids = {mem_id for mem_id, _, _ in prepared_existing}

        extractor = create_extractor(
            self.model,
            tools=list(self.schemas),
            enable_inserts=self.enable_inserts,
            enable_updates=self.enable_updates,
            enable_deletes=self.enable_deletes,
            existing_schema_policy=False,
        )
        # initial payload uses the full prepared_existing list
        payload = {"messages": prepared_messages, "existing": prepared_existing}
        # Use a dict to record the latest update for each memory id.
        results: dict[str, BaseModel] = {}

        for i in range(max_steps):
            if i == 1:
                extractor = create_extractor(
                    self.model,
                    tools=list(self.schemas) + [Done],
                    enable_inserts=self.enable_inserts,
                    enable_updates=self.enable_updates,
                    enable_deletes=self.enable_deletes,
                    existing_schema_policy=False,
                )
            response = await extractor.ainvoke(payload, config=config)
            is_done = False
            step_results = {}
            for r, rmeta in zip(response["responses"], response["response_metadata"]):
                if hasattr(r, "__repr_name__") and r.__repr_name__() == "Done":
                    is_done = True
                    continue
                mem_id = (
                    r.json_doc_id
                    if hasattr(r, "__repr_name__") and r.__repr_name__() == "RemoveDoc"
                    else rmeta.get("json_doc_id", str(uuid.uuid4()))
                )
                step_results[mem_id] = r
            results.update(step_results)

            for mem_id, _, mem in prepared_existing:
                if mem_id not in results:
                    results[mem_id] = mem

            ai_msg = response["messages"][-1]
            if is_done or not ai_msg.tool_calls:
                break
            if i < max_steps - 1:
                actions = [
                    (
                        "updated"
                        if rmeta.get("json_doc_id")
                        else (
                            "deleted"
                            if hasattr(r, "__repr_name__")
                            and r.__repr_name__() == "RemoveDoc"
                            else "inserted"
                        )
                    )
                    for r, rmeta in zip(
                        response["responses"], response["response_metadata"]
                    )
                ]
                prepared_messages = (
                    prepared_messages
                    + [response["messages"][-1]]
                    + [
                        {
                            "role": "tool",
                            "content": f"Memory {rid} {action}.",
                            "tool_call_id": tc["id"],
                        }
                        for tc, ((rid, _), action) in zip(
                            ai_msg.tool_calls, zip(list(step_results.items()), actions)
                        )
                    ]
                )
                # For the next iteration payload, drop all removal objects.
                payload = {
                    "messages": prepared_messages,
                    "existing": self._filter_response(
                        list(results.items()), external_ids, exclude_removals=True
                    ),
                }

        # For the final response, include removals only if they refer to an external memory.
        return self._filter_response(
            list(results.items()), external_ids, exclude_removals=False
        )

    def invoke(
        self,
        input: MemoryState,
        config: typing.Optional[RunnableConfig] = None,
        **kwargs: typing.Any,
    ) -> list[ExtractedMemory]:
        max_steps = input.get("max_steps")
        if max_steps is None:
            max_steps = 1
        messages = input["messages"]
        existing = input.get("existing")
        prepared_messages = self._prepare_messages(messages, max_steps)
        prepared_existing = self._prepare_existing(existing)
        # Track external memory IDs (those passed in from outside)
        external_ids = {mem_id for mem_id, _, _ in prepared_existing}

        extractor = create_extractor(
            self.model,
            tools=list(self.schemas),
            enable_inserts=self.enable_inserts,
            enable_updates=self.enable_updates,
            enable_deletes=self.enable_deletes,
            existing_schema_policy=False,
        )
        payload = {"messages": prepared_messages, "existing": prepared_existing}
        # Use a dict to record the latest update for each memory id.
        results: dict[str, BaseModel] = {}

        for i in range(max_steps):
            if i == 1:
                extractor = create_extractor(
                    self.model,
                    tools=list(self.schemas) + [Done],
                    enable_inserts=self.enable_inserts,
                    enable_updates=self.enable_updates,
                    enable_deletes=self.enable_deletes,
                    existing_schema_policy=False,
                )
            response = extractor.invoke(payload, config=config)
            is_done = False
            step_results: dict[str, BaseModel] = {}
            for r, rmeta in zip(response["responses"], response["response_metadata"]):
                if hasattr(r, "__repr_name__") and r.__repr_name__() == "Done":
                    is_done = True
                    continue
                mem_id = (
                    r.json_doc_id
                    if (
                        hasattr(r, "__repr_name__") and r.__repr_name__() == "RemoveDoc"
                    )
                    else rmeta.get("json_doc_id", str(uuid.uuid4()))
                )
                step_results[mem_id] = r
            results.update(step_results)

            # Ensure any memory from the initial payload that hasn't been updated is retained.
            for mem_id, _, mem in prepared_existing:
                if mem_id not in results:
                    results[mem_id] = mem

            ai_msg = response["messages"][-1]
            if is_done or not ai_msg.tool_calls:
                break
            if i < max_steps - 1:
                actions = [
                    (
                        "updated"
                        if rmeta.get("json_doc_id")
                        else (
                            "deleted"
                            if (
                                hasattr(r, "__repr_name__")
                                and r.__repr_name__() == "RemoveDoc"
                            )
                            else "inserted"
                        )
                    )
                    for r, rmeta in zip(
                        response["responses"], response["response_metadata"]
                    )
                ]
                prepared_messages = (
                    prepared_messages
                    + [response["messages"][-1]]
                    + [
                        {
                            "role": "tool",
                            "content": f"Memory {rid} {action}.",
                            "tool_call_id": tc["id"],
                        }
                        for tc, ((rid, _), action) in zip(
                            ai_msg.tool_calls, zip(list(step_results.items()), actions)
                        )
                    ]
                )
                payload = {
                    "messages": prepared_messages,
                    "existing": self._filter_response(
                        list(results.items()), external_ids, exclude_removals=True
                    ),
                }

        return self._filter_response(
            list(results.items()), external_ids, exclude_removals=False
        )

    async def __call__(
        self,
        messages: typing.Sequence[AnyMessage],
        existing: typing.Optional[typing.Sequence[ExtractedMemory]] = None,
    ) -> list[ExtractedMemory]:
        input: MemoryState = {"messages": messages}
        if existing is not None:
            input["existing"] = existing
        return await self.ainvoke(input)

    def _prepare_messages(
        self, messages: list[AnyMessage], max_steps: int = 1
    ) -> list[dict]:
        id_ = str(uuid.uuid4())
        session = (
            f"\n\n<session_{id_}>\n{utils.get_conversation(messages)}\n</session_{id_}>"
        )
        if max_steps > 1:
            session = f"{session}\n\nYou have a maximum of {max_steps - 1} attempts"
            " to form and consolidate memories from this session."
        return [
            {"role": "system", "content": "You are a memory subroutine for an AI."},
            {
                "role": "user",
                "content": (
                    f"{self.instructions}\n\nEnrich, prune, and organize memories based on any new information. "
                    f"If an existing memory is incorrect or outdated, update it based on the new information. "
                    f"All operations must be done in single parallel multi-tool call."
                    f" Avoid duplicate extractions. {session}"
                ),
            },
        ]

    def _prepare_existing(
        self,
        existing: typing.Optional[
            typing.Union[
                list[str], list[tuple[str, BaseModel]], list[tuple[str, str, dict]]
            ]
        ],
    ) -> list[tuple[str, str, typing.Any]]:
        if existing is None:
            return []
        if all(isinstance(ex, str) for ex in existing):
            MemoryModel = self.schemas[0]
            return [
                (str(uuid.uuid4()), "Memory", MemoryModel(content=ex))
                for ex in existing
            ]
        result = []
        for e in existing:
            if isinstance(e, (tuple, list)) and len(e) == 3:
                result.append(tuple(e))
            else:
                # Assume a two-element tuple: (id, value)
                id_, value = e[0], e[1]
                kind = (
                    value.__repr_name__() if isinstance(value, BaseModel) else "__any__"
                )
                result.append((id_, kind, value))
        return result

    @staticmethod
    def _filter_response(
        memories: list[ExtractedMemory],
        external_ids: set[str],
        exclude_removals: bool = False,
    ) -> list[ExtractedMemory]:
        """
        When exclude_removals is True (for the next iteration payload),
        drop any memory whose content is a RemoveDoc.
        When False (final response), drop removal objects only for internal memories.
        """
        results = []
        for rid, value in memories:
            is_removal = (
                hasattr(value, "__repr_name__") and value.__repr_name__() == "RemoveDoc"
            )
            if exclude_removals:
                if is_removal:
                    continue
            else:
                # Final response: if this is a removal *and* its id is not external, skip it.
                if is_removal and (rid not in external_ids):
                    continue
            results.append(ExtractedMemory(id=rid, content=value))
        return results


def create_memory_manager(
````


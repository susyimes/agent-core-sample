# MASAI five sub-agent architecture spec (paper Section 2)

Title: MASAI five sub-agent architecture spec (paper Section 2)
Source-URL: https://arxiv.org/html/2406.11638v1
Source-Repo-or-Site: arXiv:2406.11638 (Microsoft Research India)
Original-Path: Section 2 MASAI Agent Architecture incl. 2.3 Agent Instantiation (verbatim section extraction, HTML rendering; full paper at Source-URL)
Category: 29-software-repair-research
Tags: masai, modular-agents, test-generation, localization, ranking, paper
Retrieved: 2026-11-08
Value-Note: No public MASAI code repository was found on 2026-11-08, so the paper is the canonical prompt spec: five sub-agents (Test Template Generator, Issue Reproducer, Edit Localizer, Fixer, Ranker) each with objective, inputs, allowed actions and output contract. Modularity as judgement decomposition.

--- ORIGINAL ---

## 2 MASAI Agent Architecture

Solving a problem in a code repository requires understanding the problem description and the codebase, gathering the necessary information scattered across multiple files, locating the root cause, fixing it and verifying the fix. Instead of treating this as one long chain of reasoning and actions, we propose modularizing the problem into sub-problems and delegating them to different sub-agents.

![Refer to caption](2406.11638v1/detailed_overview.png)

Figure 2: MASAI applied to the task of repository-level issue resolution on an example. MASAI takes a repository and an issue description as input, and produces a single patch. The 5 sub-agents (thick borders) tackle different sub-problems. The information flow between them is shown by directed edges. They marked with the solution strategy and input 鈻竆\blacktriangleright output specification  
Detail: The example issue from the scikit-learn repository (id: 13142) describes inconsistent behaviour between two functions relating to GaussianMixture and gives an example. The Test Template Generator first generates an example test case along with the command to run the test case. This is given to the Issue Reproducer which writes a test that reproduces the issue along with the command to run it. The Edit Localizer navigates the repository to find files related to the buggy behaviour of GaussianMixture and passes the information to the Fixer which generates a set of possible patches which could fix the issue. Finally, the Ranker takes in the possible patches and the generated reproductions test. Running the tests on the patches, the ranker observes that one of the patches pass while the rest patch fail. It outputs the ranking with the passing patch first which gets selected as the proposed solution.

### 2.1 Agent Specification and Composition

A MASAI *agent* is a composition of several MASAI *sub-agents*. A MASAI *sub-agent* is specified by a tuple 鉄ㄢ€婭鈥媙鈥媝鈥媢鈥媡,鈥婼鈥媡鈥媟鈥媋鈥媡鈥媏鈥媑鈥媦,鈥婳鈥媢鈥媡鈥媝鈥媢鈥媡鉄‐\langle\\emph{Input},\\emph{Strategy},\\emph{Output}\\rangle where

1.  1.

    *Input* to the sub-agent comprises of the code repository, information obtained from other sub-agents as necessary, a set of allowed actions and task instructions.

2.  2.

    *Strategy* is the problem-solving strategy to be followed by the sub-agent in using the LLM to solve its given sub-problem. This could be vanilla completion, CoT聽([Wei et聽al., 2022](#bib.bib37 "")), ReAct聽([Yao et聽al., 2023](#bib.bib42 "")), RAG聽([Lewis et聽al., 2020](#bib.bib18 "")), etc.;

3.  3.

    *Output* is the specification of the content that the sub-agent must return upon completion as well the format it must be presented in.

Compared to multi-agent frameworks聽([Wu et聽al., 2023](#bib.bib39 ""); [Qian et聽al., 2023](#bib.bib26 ""); [Hong et聽al., 2024](#bib.bib13 "")), the MASAI architecture is simpler, in that, the sub-agents are given modular objectives that do not require explicit one-to-one or group conversations between sub-agents. The sub-agents are composed by passing the output from one sub-agent to the input of another sub-agent.

### 2.2 Action Space

All the sub-agents are presented with a set of actions which allows them to interact with the environment. The actions we use in this work are:

1.  1.

    READ(file, class, function): Query and read a specific function, class or file. All three attributes are not necessary; the agent can specify only a function and a file or even a single file. If there exists only one exactly matching code segment with these attributes, then that code is returned. If there are multiple matches, all their names are returned and the query can be refined if necessary. The READ action returns a lazy representation that aims to keep the output concise. When reading a file, only signatures of the top level definitions are presented; when reading a class, the signature of the class (class name and member signatures) are presented and when reading a function, its complete body is presented.

2.  2.

    EDIT(file, class, function): Marks a code segment for editing. Just like READ, this marks a code segment only when a unique match exists. Otherwise, the set of partial matches are returned which may be refined further.

3.  3.

    ADD(file): Marks a file for code addition. The file must exist for the action to succeed.

4.  4.

    WRITE(file, contents): Writes the specified content to a file. The specified file can be new or a file that the agent has created earlier.

5.  5.

    LIST(folder): Lists folder contents if it exists.

6.  6.

    COMMAND(command): Executes the command in a shell with timeout and truncation of large results.

7.  7.

    DONE: Used by the agent to signal that it has completed its assigned objective.

### 2.3 Agent Instantiation

In this work, we focus on the general task of resolving repository-level issues, as exemplified by the SWE-bench Lite dataset. A problem statement consists of an issue description and a repository. The agent is required to produce a patch so that the issue is resolved. Issue resolution is checked by ensuring that the relevant, held-out test cases pass. Below, we refer to ReAct聽[Yao et聽al. (2023)](#bib.bib42 "") which is a problem-solving strategy that alternates between generating an action to take using an LLM followed by executing the action and using the resulting observations as input for the subsequent action generation. Chain of Thought (CoT)聽[Wei et聽al. (2022)](#bib.bib37 "") generates solutions to a problem using an LLM while asking it to generate specific intermediate reasoning steps.

We instantiate 5 sub-agents to collectively resolve repository-level issues. Figure聽[2](#S2.F2 "Figure 2 鈥?2 MASAI Agent Architecture 鈥?MASAI: Modular Architecture for Software-engineering AI Agents") shows the overall architecture of our MASAI agent on a concrete example, along with the information flow between the sub-agents (shown by the solid edges).

(1) Test Template Generator: Discovers how to write and run a new test by analyzing the testing setup specific to the repository.

*   鈥?
    *Input*: The repository state (within its execution environment) is provided. READ, LIST, COMMAND, WRITE and DONE actions are provided.

*   鈥?
    *Strategy*: ReAct.

*   鈥?
    *Output*: The code for a template test case (which is issue independent) for the repository along with the command to run it. This is used to aid the Issue Reproducer sub-agent described next.

Test Template Generator is instructed to explore the documentation and existing tests within the repository to complete its objective and to keep trying until it comes up with a template and a command that passes without exceptions. Test Template Generator evaluates the output of its ReAct loop to determine whether the generated test passes without exceptions. It retries upto a specified limit or until it finds a template that works.

(2) Issue Reproducer: Writes a test that reproduces the behaviour reported in the given issue.

*   鈥?
    *Input*: In addition to the repository state and issue description, the sample test file and the command to run it, generated by the Test Template Generator, are provided. Actions available are READ, LIST, COMMAND, WRITE and DONE.

*   鈥?
    *Strategy*: ReAct.

*   鈥?
    *Output*: The code for a test case which reproduces the issue and would show a change in status (pass vs. fail) when the issue is fixed. It also outputs the shell command to run the test.

(3) Edit Localizer: Navigates the repository and identifies code locations (files, classes, functions) that need to be edited to resolve the issue.

*   鈥?
    *Input*: The repository state and the issue description are provided. Available actions are READ, LIST, EDIT, ADD, COMMAND and DONE.

*   鈥?
    *Strategy*: ReAct.

*   鈥?
    *Output*: List of code locations (specified through the EDIT and ADD commands) to edit.

If no locations have been marked at the end of the ReAct loop, then the Edit Localizer selects a set of locations from all of the ones it has read so far.

(4) Fixer: Suggests multiple potential patches to the code locations marked by Edit Localizer that may resolve the issue.

*   鈥?
    *Input*: Issue description along with contents of the code locations required to be edited. No actions are given to this sub-agent.

*   鈥?
    *Strategy*: CoT.

*   鈥?
    *Output*: Multiple possible candidate patches to the provided suspicious code.

When prompting the LLM for a possible patch, Fixer asks for the edit in the form of a minimal rewrite instead of rewriting the full sections. Similar to聽[Deligiannis et聽al. (2023)](#bib.bib10 ""), the content of the locations to edit are provided by Fixer with line numbers. For each edit, the Fixer expects the LLM to output the original version of the code snippet (pre) followed by the edited version of this snippet (post). Both these snippets are expected to have a line number for each line. Fixer then searches for the pre snippet using line numbers in the target file to replace with the post version. If an exact match is not found, it uses fuzzy matching to find the closest matching span for the pre snippet. After replacing with the post span, it computes the diff of the target file with its contents before the edit. Syntactically incorrect edits are rejected and the resultant patches are used downstream.

(5) Ranker: Ranks the candidate patches from the Fixer, using the test generated by Issue Reproducer.

*   鈥?
    *Input*: Issue description, candidate patches from Fixer, and the reproduction test (as well as the command to run it) from Issue Reproducer. No environment actions are allowed.

*   鈥?
    *Strategy*: CoT.

*   鈥?
    *Output*: Ranking of the candidate patches in the order of likelihood to resolve the issue.

For each of the patches, Ranker first runs the test on each of the patches and then asks the LLM to determine whether the application of that patch to the repository has caused the provided test to change status (go from failing to passing or vice versa) given the test results. Based on the output of this, the LLM is then asked to rank the patches. The top ranked patch is selected as the issue resolution. If the Issue Reproducer sub-agent could not generate a test, then the Ranker ranks the patches using only the issue description.


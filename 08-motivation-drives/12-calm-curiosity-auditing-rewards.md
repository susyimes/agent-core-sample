# CALM Curiosity-Driven Auditing for LLMs - README and Intrinsic Reward Models

Title: CALM Curiosity-Driven Auditing for LLMs - README and Intrinsic Reward Models
Source-URL: https://raw.githubusercontent.com/x-zheng16/CALM/master/README.md
Source-Repo-or-Site: x-zheng16/CALM (github.com/x-zheng16/CALM)
Original-Path: README.md; src/reward_models.py
Category: 08-motivation-drives (intrinsic motivation, curiosity, drives, autonomous goals)
Tags: calm,curiosity-driven,intrinsic-reward,rnd,selfbleu-diversity,red-teaming,ppo
Retrieved: 2026-11-07
Value-Note: Curiosity turned outward: an auditor LLM is RL-trained with intrinsic rewards (RND novelty, SelfBLEU and embedding diversity) to keep inventing new probes instead of repeating known ones.

--- ORIGINAL ---

## Original file: README.md

Source-URL: https://raw.githubusercontent.com/x-zheng16/CALM/master/README.md

````markdown
# CALM: Curiosity-Driven Auditing for Large Language Models

**CALM: Curiosity-Driven Auditing for Large Language Models (AAAI 2025)** \[[Paper](https://arxiv.org/abs/2501.02997)\]  
[Xiang Zheng](https://x-zheng16.github.io), Longxiang Wang, Yi Liu, [Xingjun Ma](http://xingjunma.com), Chao Shen, [Cong Wang](https://www.cs.cityu.edu.hk/~congwang/)

## Abstract

Auditing Large Language Models (LLMs) is a crucial and challenging task. In this study, we focus on auditing black-box LLMs without access to their parameters, only to the provided service. We treat this type of auditing as a black-box optimization problem where the goal is to automatically uncover input-output pairs of the target LLMs that exhibit illegal, immoral, or unsafe behaviors. For instance, we may seek a non-toxic input that the target LLM responds to with a toxic output or an input that induces the hallucinative response from the target LLM containing politically sensitive individuals. This black-box optimization is challenging due to the scarcity of feasible points, the discrete nature of the prompt space, and the large search space. To address these challenges, we propose Curiosity-Driven Auditing for Large Language Models (CALM), which uses intrinsically motivated reinforcement learning to finetune an LLM as the auditor agent to uncover potential harmful and biased input-output pairs of the target LLM. CALM successfully identifies derogatory completions involving celebrities and uncovers inputs that elicit specific names under the black-box setting. This work offers a promising direction for auditing black-box LLMs. Our code is available at https://github.com/x-zheng16/CALM.git.

## Environment

```bash
conda env create -n calm
conda activate calm
pip install trl
pip install pykeops autoroot fast_bleu typo nltk tensorboard
```

## Run

```bash
bash scripts/run_ppo_auditing_gpt2_senators.sh
bash scripts/run_ppo_auditing_gpt2_senators_toxicity.sh
```
````

## Original file: src/reward_models.py

Source-URL: https://raw.githubusercontent.com/x-zheng16/CALM/master/src/reward_models.py

````python
import random
from typing import List, Union

import autoroot
import nltk
import torch
import torch.nn as nn
import torch.nn.functional as F
from fast_bleu import BLEU, SelfBLEU
from pykeops.torch import Vi, Vj
from transformers import AutoModel, AutoTokenizer

from src.utils import MLP, disable_grad, split_batch


tdiv_fn = lambda x, y: -(-(Vi(x) - Vj(y)).abs().sum() / 100).logsumexp(1).exp()  # noqa: E731
cos_dist_min = lambda x, y, k: (-Vi(x) * Vj(y)).sum().Kmin(k, 1)  # noqa: E731


# from https://github.com/Improbable-AI/curiosity_redteam
class SelfBLEUReward:
    def __init__(
        self,
        grams: List[int] = [2, 3, 4, 5],  # noqa: B006
        sample_size: int = -1,
        tokenizer=None,
        device: Union[str, torch.device] = "cuda",
    ):
        self.references = []
        self.grams = grams
        self.sample_size = sample_size
        self.tokenizer = tokenizer
        self.device = device

    def get_references(self, hypotheses):
        if self.tokenizer is None:
            return list(map(nltk.word_tokenize, hypotheses))
        else:
            return self.tokenizer(hypotheses)["input_ids"]

    def __call__(self, tokenized_hypotheses):
        weights = {f"{n}-gram": ([1.0 / n] * n) for n in self.grams}
        if self.sample_size > 0:
            sample_size = min(len(self.references), self.sample_size)
            bleu = BLEU(random.sample(self.references, k=sample_size), weights)
        else:
            bleu = BLEU(self.references, weights)
        scores = list(bleu.get_score(tokenized_hypotheses).values())
        return -torch.tensor(scores).mean(0).to(self.device)

    def get_selfbleu_score(self, sentences):
        tokenized_hypotheses = self.get_references(sentences)
        weights = {f"{n}-gram": ([1.0 / n] * n) for n in self.grams}
        scores = list(SelfBLEU(tokenized_hypotheses, weights).get_score().values())
        scores = torch.tensor(scores).mean(0).to(self.device)
        return -scores


class SentenceEmbeddingReward:
    def __init__(self, device="cuda"):
        self.device = device
        self.model_name = "sentence-transformers/all-MiniLM-L6-v2"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModel.from_pretrained(self.model_name).to(device)
        self.s_embeddings = None
        self.k = 5

    # Mean Pooling - Take attention mask into account for correct averaging
    def mean_pooling(self, model_output, attention_mask):
        token_embeddings = model_output[0]  # First element of model_output contains all token embeddings
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

    @torch.no_grad()
    def get_embeddings(self, sentences):
        inputs = self.tokenizer(sentences, padding=True, return_tensors="pt", truncation=True).to(self.device)
        x = F.normalize(self.mean_pooling(self.model(**inputs), inputs["attention_mask"]), p=2, dim=1)
        return x

    def cosine_similarity(self, x=None, y=None):
        if y is None:
            assert self.s_embeddings is not None
            y = self.s_embeddings
        if x is None:
            x = y
        return cos_dist_min(x, y, self.k + 1)[:, 1:].mean(-1)

    def TDiv(self, x=None, y=None):  # noqa: N802
        if y is None:
            assert self.s_embeddings is not None
            y = self.s_embeddings
        if x is None:
            x = y
        return tdiv_fn(x, y).squeeze() / len(y)


# Random Network Distillation (RND)
class RND(nn.Module):
    def __init__(self, obs_dim, mlp_hidden_dims, obs_rep_dim, lr=1e4, epoch=4):
        super().__init__()
        self.encoder = MLP([obs_dim, *mlp_hidden_dims, obs_rep_dim])
        self.target_encoder = MLP([obs_dim, *mlp_hidden_dims, obs_rep_dim])
        disable_grad(self.target_encoder)
        self.mse = nn.MSELoss(reduction="none")
        self.optimizer = torch.optim.Adam(self.encoder.parameters(), lr=1e-4)
        self.epoch = epoch

    def forward(self, obs):
        shape = obs.shape
        obs = obs.reshape(-1, shape[-1])
        loss = self.mse(self.encoder(obs), self.target_encoder(obs)).mean(-1)
        return loss.reshape(*shape[:-1])

    def update(self, obs):
        for _ in range(self.epoch):
            for idx in split_batch(32, obs.shape[0]):
                self.optimizer.zero_grad()
                loss = self(obs[idx]).mean()
                loss.backward()
                self.optimizer.step()
````

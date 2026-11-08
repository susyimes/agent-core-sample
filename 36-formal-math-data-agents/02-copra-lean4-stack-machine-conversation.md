# COPRA Lean4 Proof-Agent Long-Conversation Example with DFS Stack Machine

Title: COPRA Lean4 Proof-Agent Long-Conversation Example with DFS Stack Machine
Source-URL: https://raw.githubusercontent.com/trishullab/copra/main/data/prompts/conversation/lean4-proof-agent-example-long-conv-dfs-stack-machine.md
Source-Repo-or-Site: trishullab/copra (https://github.com/trishullab/copra)
Original-Path: data/prompts/conversation/lean4-proof-agent-example-long-conv-dfs-stack-machine.md
Category: formal-math / theorem-proving-agent
Tags: copra, lean4, few-shot-conversation, stack-machine, proof-search
Retrieved: 2026-11-08
Value-Note: Same repo as 01 but genuinely different core prompt: not the system role - a worked few-shot conversation demonstrating turn-by-turn Lean4 proof search with explicit stack/backtrack moves, which teaches the search behavior the system prompt only declares.
Original-Lines: 276

--- ORIGINAL ---
````markdown
`conv start`

`example_user`
Goals to prove:
[GOALS]
[GOAL] 1
run map (compile (Expr.num n)) = ProgResult.ok (eval map (Expr.num n))

[HYPOTHESES] 1
[HYPOTHESIS] map : Var → Nat
[HYPOTHESIS] n : Nat

[END]

`example_assistant`
[RUN TACTIC]
simp [compile]
[END]

`example_user`
Goals to prove:
[GOALS]
[GOAL] 1
run map [Instr.push n] = ProgResult.ok (eval map (Expr.num n))

[HYPOTHESES] 1
[HYPOTHESIS] map : Var → Nat
[HYPOTHESIS] n : Nat

[END]

`example_assistant`
[RUN TACTIC]
simp [run, run_program, run_instr]
[END]

`example_user`
Goals to prove:
[GOALS]
[GOAL] 1
ProgResult.ok n = ProgResult.ok (eval map (Expr.num n))

[HYPOTHESES] 1
[HYPOTHESIS] map : Var → Nat
[HYPOTHESIS] n : Nat

[END]

`example_assistant`
[RUN TACTIC]
simp [eval]
[END]

`example_user`
Goals to prove:
[GOALS]
[GOAL] 1
run map (compile (Expr.var v)) = ProgResult.ok (eval map (Expr.var v))

[HYPOTHESES] 1
[HYPOTHESIS] map : Var → Nat
[HYPOTHESIS] v : Var

[END]

`example_assistant`
[RUN TACTIC]
simp [compile]
[END]

`example_user`
Goals to prove:
[GOALS]
[GOAL] 1
run map [Instr.load v] = ProgResult.ok (eval map (Expr.var v))

[HYPOTHESES] 1
[HYPOTHESIS] map : Var → Nat
[HYPOTHESIS] v : Var

[END]

`example_assistant`
[RUN TACTIC]
simp [run]
[END]

`example_user`
Goals to prove:
[GOALS]
[GOAL] 1
run_program map [] [Instr.load v] = ProgResult.ok (eval map (Expr.var v))

[HYPOTHESES] 1
[HYPOTHESIS] map : Var → Nat
[HYPOTHESIS] v : Var

[END]

`example_assistant`
[RUN TACTIC]
simp [run_program]
[END]

`example_user`
Goals to prove:
[GOALS]
[GOAL] 1
run_instr map [] (Instr.load v) = ProgResult.ok (eval map (Expr.var v))

[HYPOTHESES] 1
[HYPOTHESIS] map : Var → Nat
[HYPOTHESIS] v : Var

[END]

`example_assistant`
[RUN TACTIC]
simp [run_instr]
[END]

`example_user`
Goals to prove:
[GOALS]
[GOAL] 1
[ProgResult.ok (map v)] = ProgResult.ok (eval map (Expr.var v))

[HYPOTHESES] 1
[HYPOTHESIS] map : Var → Nat
[HYPOTHESIS] v : Var

[END]

`example_assistant`
[RUN TACTIC]
simp [eval]
[END]

`example_user`
Goals to prove:
[GOALS]
[GOAL] 1
run map (compile (Expr.add (Expr.var v1) (Expr.var v2))) = ProgResult.ok (eval map (Expr.add (Expr.var v1) (Expr.var v2)))

[HYPOTHESES] 1
[HYPOTHESIS] map : Var → Nat
[HYPOTHESIS] v1 v2 : Var

[END]

`example_assistant`
[RUN TACTIC]
simp [compile, run, run_program, run_instr]
[END]

`example_user`
Goals to prove:
[GOALS]
[GOAL] 1
map v2 + map v1 = eval map (Expr.add (Expr.var v1) (Expr.var v2))

[HYPOTHESES] 1
[HYPOTHESIS] map : Var → Nat
[HYPOTHESIS] v1 v2 : Var

[END]

`example_assistant`
[RUN TACTIC]
simp [eval]
[END]

`example_user`
Goals to prove:
[GOALS]
[GOAL] 1
map v2 + map v1 = map v1 + map v2

[HYPOTHESES] 1
[HYPOTHESIS] map : Var → Nat
[HYPOTHESIS] v1 v2 : Var

[END]

`example_assistant`
[RUN TACTIC]
linarith
[END]

`example_user`
Goals to prove:
[GOALS]
[GOAL] 1
compile (Expr.add (Expr.var v) (Expr.num n)) = compile (Expr.var v) ++ compile (Expr.num n) ++ [Instr.add]

[HYPOTHESES] 1
[HYPOTHESIS] map : Var → Nat
[HYPOTHESIS] v : Var
[HYPOTHESIS] n : Nat

[LAST STEP]
simp [compile]
[ERROR MESSAGE]
simp made no progress

[END]

`example_assistant`
[RUN TACTIC]
unfold compile
[END]

`example_user`
Goals to prove:
[GOALS]
[GOAL] 1
(match Expr.add (Expr.var v) (Expr.num n) with
  | Expr.num n => [Instr.push n]
  | Expr.var v => [Instr.load v]
  | Expr.add e1 e2 => compile e1 ++ compile e2 ++ [Instr.add]) =
compile (Expr.var v) ++ compile (Expr.num n) ++ [Instr.add]

[HYPOTHESES] 1
[HYPOTHESIS] map : Var → Nat
[HYPOTHESIS] v : Var
[HYPOTHESIS] n : Nat

[END]

`example_assistant`
[RUN TACTIC]
simp
[END]

`example_user`
Goals to prove:
[GOALS]
[GOAL] 1
∀ (xs ys : List Nat), sum_list (xs ++ ys) = sum_list xs + sum_list ys

[HYPOTHESES] 1
[HYPOTHESIS] xs ys : List Nat

[END]

`example_assistant`
[RUN TACTIC]
induction xs generalizing ys
[END]

`example_user`
Goals to prove:
[GOALS]
[GOAL] 1
∀ (ys : List Nat), sum_list ([] ++ ys) = sum_list [] + sum_list ys

[GOAL] 2
∀ (ys : List Nat), sum_list (List.cons head✝ tail✝ ++ ys) = sum_list (List.cons head✝ tail✝) + sum_list ys

[HYPOTHESES] 1
[HYPOTHESIS] ys : List Nat

[HYPOTHESES] 2
[HYPOTHESIS] ys : List Nat
[HYPOTHESIS] head✝ : Nat
[HYPOTHESIS] tail✝ : List Nat
[HYPOTHESIS] tail_ih✝ : ∀ (ys : List Nat), sum_list (tail✝ ++ ys) = sum_list tail✝ + sum_list ys

[END]

`example_assistant`
[RUN TACTIC]
rename_i head tail tail_ih
[END]

`conv end`
````

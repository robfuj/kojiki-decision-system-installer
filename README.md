# 22 — Decision System Installer

> Part of the **Kojiki Decision System**. This repo is the
> **Decision System Installer** line. It references the shared ontology in
> [`00-kojiki-ontology`](https://github.com/robfuj/kojiki-ontology) for the
> canonical schemas, taxonomy, decision-rights, and handoff standards.

## Primary question
> Which executive agents should be installed, and how should the chosen decision system be scaffolded?

## Purpose
Meta-installer: brings the shared ontology + the 20 line repos + the org-builder together, asks the user which executive agents they want to install, and scaffolds a working multi-agent workspace with the handoff registry wired so agents can communicate.

## Sub-functions
Discovery, Selection Prompt, Workspace Scaffold, Registry Wiring, Orientation Orchestration, Validation

## Typical roles
Installer Agent, User (human or parent agent)

## Inputs
The 21 source repos (ontology + 20 lines + org-builder); user's selection of executive agents; orientation answers (industry, jurisdiction, etc.).

## Outputs
A scaffolded workspace: chosen line repos + 00-kojiki-ontology, a populated handoffs/registry.json, an orientation state file, and a run order for cross-functional decisions.

## Learning focus
Which agent selections matched the org's needs; which agents were never used; scaffold gaps discovered during operation.

## Operating tree
```text
DISCOVER REPOS →
 PRESENT OPTIONS →
 USER SELECTS →
 SCAFFOLD WORKSPACE →
 WIRE REGISTRY →
 RUN ORIENTATION →
 VALIDATE →
 HANDOFF READY
```

## Decision states
```text
DISCOVERING → PRESENTING → SELECTING → SCAFFOLDING → WIRING → ORIENTING → VALIDATED → READY
```

## Decision outputs
`Install All · Install Subset · Install With Org-Builder · Defer · Abort`

## Critical prompts (what this function thinks about)
> Which executive agents does the user want to install?
> Should the org-builder run first?
> Which lines are mandatory for this org?
> Where should the workspace live?
> How are agents wired to communicate?
> What validates a correct install?

## Canonical record schema (Learning Ledger + Decision Object Fields)
Every decision in this line is recorded as:
- a **Decision Object** — see `schema/decision-object.json`
- a **Learning Ledger** entry — see `schema/learning-ledger.json`

and the agent must run the **Orientation Protocol** first (see `AGENT.md`).

## How this line runs on SYNAPSIS (the cognitive substrate)
Every decision in this line is decomposed through the shared SYNAPSIS transformation
chain ([`00-kojiki-ontology/synapsis`](https://github.com/robfuj/kojiki-ontology/synapsis)):
```
SOURCE → RECORD → EVIDENCE → INTERPRETATION → STRATEGY → INTERACTION → OUTPUT → OUTCOME → LEARNING
```
- **Three steps are dedicated niche bots**: `bots/evidence/` (this line's extraction
 specialist); the shared `synapsis/audit-bot/` (independent audit, org-wide) and
 `synapsis/learning-bot/` (cross-line memory). See `AGENT.md` for the full contract.
- The rest run inline inside this line's agent, each bounded to one authority.
- Meta-rule: *evidence ≠ interpretation ≠ belief ≠ doctrine.* Validate with
 `python3 synapsis/validate.py <record.json>` (in the ontology repo).

## How to use
1. Read `AGENT.md` — the first-run Orientation Protocol.
2. Read `SCHEMA.md` — how this line maps to the universal schema.
3. Read `data/22-decision-system-installer.json` — the machine-readable spec.
4. See `data/example.json` — one fully worked decision (Decision Object + Ledger).
5. Use `decision-graph.mmd` — agent-decodable operating tree + state model.
6. Validate new records: `python3 tools/validate.py data/<name>.json`

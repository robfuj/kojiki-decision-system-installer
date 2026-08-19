#!/usr/bin/env python3
"""Harness-agnostic scaffold: given a selection of agent keys, copy the matching
repos + 00-kojiki-ontology into a workspace and prime handoffs/registry.json.

Usage:
    python3 scripts/scaffold.py --keys 01 02 04 15 16 21 --out ./workspace
"""
import os, sys, json, shutil, argparse

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--keys", nargs="+", required=True, help="agent keys e.g. 01 02 04")
    ap.add_argument("--out", default="./workspace")
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    # always include ontology
    sel = ["00-kojiki-ontology"] + ["%s-%s" % (k.split("-")[0], k) if "-" not in k else k for k in args.keys]
    # normalize: accept both "04" and "04-sales"
    chosen = []
    for k in args.keys:
        if "-" in k:
            chosen.append(k)
        else:
            # find repo dir starting with "NN-"
            for name in os.listdir(ROOT):
                if name.startswith(k + "-"):
                    chosen.append(name); break
    chosen = ["00-kojiki-ontology"] + chosen
    registry = []
    for name in chosen:
        src = os.path.join(ROOT, name)
        if not os.path.isdir(src):
            print("SKIP (not found):", name); continue
        dst = os.path.join(args.out, name)
        shutil.copytree(src, dst, dirs_exist_ok=True)
        registry.append({"agent_name": name, "function_line": name,
                         "group_id": "pending-orientation", "endpoint": "",
                         "registered_at": ""})
    reg_path = os.path.join(args.out, "00-kojiki-ontology", "handoffs", "registry.json")
    os.makedirs(os.path.dirname(reg_path), exist_ok=True)
    with open(reg_path, "w") as f:
        json.dump(registry, f, indent=2)
    print("Scaffolded", len(chosen), "repos into", args.out)
    print("Next: run each agent's AGENT.md Orientation Protocol; fill registry entries.")

if __name__ == "__main__":
    main()

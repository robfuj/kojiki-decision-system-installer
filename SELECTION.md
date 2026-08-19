# Installer selection prompt (harness-agnostic)

When this installer runs, it MUST ask the user (human or parent agent):

 "Which executive agents do you want to install for your organization?"

Present the available agents as a numbered list:
 00 - Shared Ontology (always included)
 01 - Executive / Strategy 02 - Finance 03 - Marketing
 04 - Sales 05 - Business Dev 06 - Customer Success
 07 - Product 08 - Engineering 09 - Operations
 10 - Supply Chain/Procure 11 - Data/Analytics 12 - AI/Intelligence
 13 - IT 14 - Security 15 - Legal
 16 - Risk/Compliance 17 - People/HR 18 - Corporate Dev
 19 - Communications 20 - Executive Office
 21 - Executive Org Builder (recommended)

Recommend a LEAN default subset based on org size + regulated status, but let the
user expand. Never silently install all 20.

After selection, scaffold the chosen repos + 00-kojiki-ontology, populate
handoffs/registry.json, and run each agent's AGENT.md Orientation Protocol in order.

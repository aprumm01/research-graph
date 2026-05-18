---
source_file: "research_docs/P527.pdf"
type: ""
community: "GenAI in UX and Design Practice"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/GenAI_in_UX_and_Design_Practice
---

# UXCascade: Scalable Usability Testing with Simulated User Agents Steffen Holt...

## Summary
Holter, Koh, Dogan, and Chan present UXCascade, an interactive system for conducting scalable usability testing using simulated user agents that browse websites, uncover usability issues, and support rapid design iteration. The system implements a multi-level analysis workflow that aggregates persona-conditioned agent runs into structured findings, links agent reasoning to specific UI elements, and enables practitioners to propose interface edits and instantly re-evaluate their impact across the full persona set. A within-subjects user study with eight UX professionals finds that UXCascade performs comparably to human-generated feedback on issue discovery, suggesting its utility as a lightweight complement to traditional usability testing.

## Key Concepts
- UXCascade: end-to-end system for simulation-based usability testing at scale
- Persona-conditioned agents: LLM agents assigned user goals and traits to simulate diverse user behaviors
- Multi-level analysis workflow: aggregates patterns across personas, goals, and outcomes into actionable insights
- Edit-in-the-loop iteration: practitioners propose interface changes; agents automatically re-evaluate the modified version
- Journey visualization: shows how a UI change affects different personas over time across interaction steps

## Theoretical Framework
Grounded in HCI usability testing literature and LLM-based agent simulation research; the work positions itself as a complement to human-centered evaluation methods (Nielsen's heuristics, think-aloud protocols), not a replacement. The evaluation uses a within-subjects study design comparing agent-generated and human-generated feedback against a seeded usability issue set.

## Methods
User study with 8 UX professionals; custom website seeded with known usability issues; participants used UXCascade and a baseline (human-generated feedback) to identify issues; measures included issue discovery rates, NASA-TLX subjective workload, and self-reported fit with existing UX workflows; results compared between conditions.

## Main Arguments
- LLM-simulated agents can detect usability issues at a rate comparable to human feedback, validating simulation as a viable early-stage evaluation option
- The multi-level structured output (goals → patterns → issues → traces) enables practitioners to move efficiently from raw agent logs to actionable findings
- Edit-in-the-loop iteration closes the feedback gap in rapid development cycles where human studies are too slow to run for every design variant
- Current simulation is not a substitute for human testing in high-stakes contexts; it is a lightweight screening tool for early-stage interface development

## Limitations & Critiques
Small user study (n=8) limits statistical power; all participants were UX professionals, so generalizability to non-expert developers is unclear; the custom seeded website may not represent the complexity of real production environments; the study does not report inter-rater reliability for issue categorization, making it hard to assess baseline quality.

## Connections
- [[GenAI in UX and Design Practice]] - `` [EXTRACTED]

#graphify/document #graphify/EXTRACTED #community/GenAI_in_UX_and_Design_Practice
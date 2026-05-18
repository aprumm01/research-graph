---
source_file: "research_docs/P524.pdf"
type: ""
community: "GenAI in UX and Design Practice"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/GenAI_in_UX_and_Design_Practice
---

# Avenir-UX: Automated UX Evaluation via Simulated Human Web Interaction with G...

## Summary
Tan, Lim, Durgad, Obegi, and Li present Avenir-UX, an open-source automated UX evaluation agent that simulates realistic human web interaction using visual GUI grounding rather than DOM parsing, enabling it to detect usability issues that depend on visual layout and interface appearance. Built on the Avenir-Web framework with a Mixture of Grounding Experts (MoGE) paradigm, the system integrates three professional UX evaluation protocols — System Usability Scale (SUS), Single Ease Questions (SEQ), and concurrent Think Aloud — to produce a structured UX report. The paper argues that visual grounding is essential for accurate automated UX evaluation, as DOM-based agents bypass the perceptual experience that makes usability problems discoverable in real user testing.

## Key Concepts
- GUI grounding: agents perceive and interact with web interfaces visually (not through DOM structure), making them susceptible to the same usability pitfalls as human users
- Mixture of Grounding Experts (MoGE): the multimodal grounding paradigm from Avenir-Web that enables robust end-to-end web interaction
- System Usability Scale (SUS): standardized 10-item usability questionnaire providing an overall usability score
- Single Ease Question (SEQ): step-wise single-item ease rating collected after each task step
- Think Aloud: agent verbalizes reasoning in real time, providing qualitative insight alongside quantitative metrics

## Theoretical Framework
Grounded in automated UX evaluation and LLM-as-judge literature; responds directly to limitations of UXAgent (Lu et al.) and DOM-based evaluation frameworks by emphasizing that visual perception is non-negotiable for usability validity. Applies MLLM-as-UI-Judge benchmarking methodology to a new interactive, end-to-end interaction paradigm rather than static screenshot analysis.

## Methods
System design paper with case study evaluation; Avenir-UX deployed against real websites; SUS, SEQ, and Think Aloud data collected from agent runs; qualitative UX report generated synthesizing quantitative scores and reasoning traces; comparison drawn to prior DOM-based and screenshot-based approaches; open-source implementation available at github.com/Onflow-AI/Avenir-UX.

## Main Arguments
- Visual grounding is necessary for UX evaluation: DOM-based agents miss style, layout, and accessibility issues that only manifest in visual rendering
- Combining SUS + SEQ + Think Aloud provides a richer, multi-dimensional evaluation than any single metric alone
- Avenir-UX enables continuous, scalable UX testing that can match the pace of agile development and AI-assisted code generation
- The democratization of app development (non-professional developers using AI tools) creates an urgent need for automated evaluation tools that don't require UX expertise or participant recruitment

## Limitations & Critiques
The paper presents a case study rather than a controlled comparative study, so there is no rigorous validation of how well agent-generated SUS/SEQ scores correlate with real user scores; the visual grounding approach may be computationally expensive and slower than DOM-based alternatives; the system's effectiveness on highly dynamic or app-like web interfaces (SPAs, WebGL, Canvas-based) is not evaluated.

## Connections
- [[GenAI in UX and Design Practice]] - `` [EXTRACTED]

#graphify/document #graphify/EXTRACTED #community/GenAI_in_UX_and_Design_Practice
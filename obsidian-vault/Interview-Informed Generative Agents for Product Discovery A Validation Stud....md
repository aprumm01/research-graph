---
source_file: "research_docs/P525.pdf"
type: ""
community: "Responsible AI and Ethics"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Responsible_AI_and_Ethics
---

# Interview-Informed Generative Agents for Product Discovery: A Validation Stud...

## Summary
Wang and Siu (Adobe Research) investigate whether interview-informed generative agents can simulate user responses in product concept testing, a novel application context where preferences are constructed on the fly for artifacts participants have never encountered. Conducting 90-minute audio interviews with knowledge workers, they create personalized agents and compare agent evaluations of four AI document workflow concepts against the same participants' actual responses (TAM, NPS, and open-ended feedback). Their key finding is that agents are "distribution-calibrated but identity-imprecise": they approximate population-level response distributions and outperform baselines at aggregate level, but fail to reliably reproduce the specific responses of the individuals they are designed to simulate.

## Key Concepts
- Distribution-calibrated but identity-imprecise: agents capture group-level tendencies but not individual-level idiosyncrasies
- Interview-informed agents: generative agents grounded in 90-minute audio interviews capturing workflow understanding and pain points, using a retrieval module and reflection component
- Product discovery: early-stage concept testing where designers need both population-level signals (which concept is promising?) and identity-level heterogeneity (which user types are excited vs. blocked?)
- TAM + NPS: Technology Acceptance Model (perceived usefulness/ease of use) and Net Promoter Score used as scalar evaluation metrics for novel AI concepts
- Concept testing with novel artifacts: unlike social science surveys testing stable attitudes, product discovery requires generating preferences for hypothetical, unseen products

## Theoretical Framework
Builds on Park et al.'s interview-informed agent architecture (85% normalized accuracy on General Social Survey) and extends it to a product discovery context. Applies a simulation fidelity evaluation framework distinguishing scalar fidelity (RQ1) from qualitative alignment (RQ2); draws on technology acceptance literature (TAM) and design research methods.

## Methods
Validation study with knowledge workers (N not specified in extracted text): 90-minute audio interviews on workflow understanding and pain points; survey on demographics and general tool usage; agent memory built from interview data using a retrieval module and reflection component; agents rate four novel AI document workflow concepts on TAM, NPS, and open-ended feedback; agent responses compared to participants' own concept test responses; analysis separated into population-level and individual-level fidelity.

## Main Arguments
- Interview-informed agents outperform baselines at the population level for product concept testing, confirming their value for early-stage directional insight
- Identity-level simulation fails: agents do not reliably reproduce the specific individual's responses even when grounded in that person's own interviews
- The distribution-calibrated but identity-imprecise pattern implies simulation is appropriate for concept screening (which concept is most promising?) but not for understanding individual workflows, adoption barriers, or trust
- Responsible integration of simulation into product discovery requires clear communication of what simulation can and cannot replace

## Limitations & Critiques
Study scope is limited to knowledge workers evaluating AI document workflow concepts at a single company (Adobe), restricting generalizability to other domains or user populations; the concept testing scenario requires constructing preferences on the fly, which is especially challenging for simulation and may explain the identity-imprecision finding more than fundamental simulation limits; qualitative alignment analysis is preliminary and not formally coded.

## Connections
- [[GenAI in UX and Design Practice]] - `` [EXTRACTED]
- [[Metacognitive Support]] - `` [EXTRACTED]
- [[Workplace Learning and AI]] - `` [EXTRACTED]

#graphify/document #graphify/EXTRACTED #community/Responsible_AI_and_Ethics
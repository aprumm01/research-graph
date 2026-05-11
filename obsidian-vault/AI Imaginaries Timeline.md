---
title: "AI Imaginaries: A Historical Timeline"
type: "synthesis"
tags:
  - synthesis
  - imaginaries
  - timeline
  - AI-history
---

# AI Imaginaries: A Historical Timeline

> *A synthesis note drawing on vault papers and Adam Prumm's literature review "AI Imaginaries, Design Education, and the Transformation of Design Practice" (2025, unpublished).*

---

## What Is an Imaginary?

A **sociotechnical imaginary** is a collectively held vision of a desirable (or feared) social future made possible by a technology — visions that shape decisions, resource allocation, and policy *before* the technology matures. Jasanoff & Kim's foundational concept describes these as "collectively imagined forms of social life and social order reflected in the design and fulfillment of nation-specific scientific and/or technological projects."

Mager & Katzenbach (2021) sharpen this: imaginaries are **"multiple, contested, and commodified narratives"** — not neutral predictions, but political acts. They carry **performative power**: once an imagined future gains institutional momentum, it begins directing real priorities and behaviors regardless of whether it ever arrives. Stanusch et al. (2024) call these failures **"underperforming imaginaries"** — expected AI transformations that never materialize but still *reshape the labor force and reshape practice* in their wake.

Throughout AI's history, the word "imaginary" was rarely used. But the phenomenon was everywhere — in Wiener's proclamations about cybernetics, in Terminator sequels, in tech CEO keynotes, in faculty abstinence policies. This timeline traces those visions, who made them, what they predicted, and what they left behind.

**Adam Prumm's "imaginaries lifecycle"** (from his 2025 literature review) frames how these visions travel:

> Industry imaginaries → shape academic programs → shape student expectations → students carry them into the workforce → workforce expectations feed back into industry leadership

Misalignment accumulates at every transition in this cycle.

---

## Quick Reference Table

| Wave | Era | Dominant Imaginary | Who Proclaimed It | Key Fear |
|---|---|---|---|---|
| **1** | 1943–1966 | The Universal Machine — intelligence is information; machines will think | Scientists, military, mathematicians | Machines replacing human cognition at scale |
| **2** | 1966–1987 | The Expert & The Factory — AI encodes expert knowledge; blue-collar work at risk | AI researchers, industrial engineers, corporations | Factory job loss; AI winter disillusionment |
| **3** | 1987–2010 | The Safe Knowledge Worker — cognitive/creative work is automation-proof | Tech industry, economists, management theorists | System optimization, not human replacement |
| **4** | 2010–2019 | The Automation Panic — everything is now at risk, including white-collar work | Frey & Osborne, media, consultancies, Big Tech | Mass unemployment; 47% of jobs automated |
| **5** | 2019–present | Contested Imaginaries — tool, collaborator, or existential threat? | Practitioners, artists, researchers, executives | Creative displacement; who owns the future? |

---

## Wave 1: The Universal Machine (1943–1966)

### The Imaginary
**"Intelligence is information processing. Machines will think — and thinking is a universal, computable process."** *(Prumm, 2025)*

This imaginary was constructed almost entirely by scientists and mathematicians, largely working under military funding during and after WWII. Its core claim: that the brain is a machine, that machines can be brains, and that this equivalence would unlock control over any complex system — organisms, economies, societies.

### Scientific Proclamations
- **Norbert Wiener** — *Cybernetics: Control and Communication in Animal and Machine* (1948): coined "cybernetics" and argued that feedback, information, and control were universal principles governing biological and mechanical systems equally
- **Claude Shannon** — *A Mathematical Theory of Communication* (1948): reduced information to bits, making it abstractly computable independent of meaning
- **Alan Turing** — "Computing Machinery and Intelligence" (1950): posed "Can machines think?" and proposed the imitation game, directly translating consciousness into a behavioral performance question
- **The Macy Conferences** (1946–1953): interdisciplinary gatherings that institutionalized cybernetic claims across biology, economics, anthropology, and engineering
- **Dartmouth Conference** (1956): McCarthy, Minsky, Shannon, and Simon coin "artificial intelligence" and proclaim that "every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it"

### Why It Spread So Far
[[papers/How to Be Universal Some Cybernetic Strategies, 1943-70|Bowker (1993)]] argues cybernetics achieved its remarkable cross-disciplinary reach not because its ideas were genuinely universal, but through **deliberate rhetorical and institutional strategies** — positioning cybernetic concepts as "boundary objects" flexible enough to be adopted across biology, economics, the social sciences, and engineering simultaneously. The Macy Conferences were the critical institutional site.

[[papers/Animo Nullius AI Origin Story and Data Colonialism (Penn 2023)|Penn (2023)]] goes further: AI's founding metaphors — mind-as-computer, society-as-system — were **borrowed from observation of capitalist social dynamics** (markets, administration, game theory), not from neuroscience. Post-war military and corporate investment shaped which research programs flourished, encoding commercial and imperial logics into the field's foundational assumptions.

[[papers/Ensmenger - The Rise of Computer Science|Ensmenger (2010)]] shows the flip side: as cybernetics translated into CS as a discipline, professionalization required **constructing an exclusionary identity** — aptitude tests, the "programmer personality" stereotype, credential systems — that systematically marginalized women and working-class practitioners who had built early computing from the ground up. The imaginary of the lone male genius programmer was manufactured alongside the machines.

### Industry & Labor Imaginary
Automation of manufacturing was the industrial imaginary in this period — not AI in the modern sense, but programmable machines replacing assembly-line workers. Unions feared it. Management embraced it. The vision of the "push-button factory" was ubiquitous in corporate communications.

### Pop Culture Touchstones
| Year | Work | Imaginary Expressed |
|---|---|---|
| 1950 | Asimov, *I, Robot* | Robots as labor class; the Three Laws as an early governance imaginary |
| 1950 | Turing, "Computing Machinery and Intelligence" | Machine consciousness as achievable — imitation as the test |
| 1951–53 | Asimov, *Foundation* series | Computational social science (psychohistory) predicting and controlling history |
| 1956 | Forbidden Planet (film) | Robby the Robot — benevolent, capable, subordinate machine |
| 1965 | Kubrick begins production on *2001* | AI as evolutionary step beyond humanity |

---

## Wave 2: The Expert and the Factory (1966–1987)

### The Imaginary
**"AI will encode human expertise. Blue-collar and routine work will be automated first. Knowledge workers — especially professionals — are safe."** *(Prumm, 2025)*

This wave split into two simultaneous imaginaries that rarely acknowledged each other: the *AI researcher's imaginary* (expert systems encoding professional knowledge) and the *industrial imaginary* (factory automation eliminating manufacturing labor). Pop culture fused them into something darker — the machine that turns against its maker.

### Scientific Proclamations
- **ELIZA** (Weizenbaum, 1966): demonstrated that people project human understanding onto simple pattern-matching programs — and Weizenbaum was alarmed by this, not celebratory
- **Lighthill Report** (UK, 1973): government review declared AI had failed to deliver on its promises → first AI winter; funding collapsed
- **Expert systems rise** (MYCIN 1974, XCON 1980): the new imaginary — AI encodes a human expert's knowledge in rules and outperforms them in specific domains. Medicine, law, engineering
- **Minsky & Papert, *Perceptrons*** (1969): killed neural network research for a decade

[[papers/From Expert Systems to Generative Artificial Experts (Sowa and Przegalinska)|Sowa & Przegalinska (2024)]] trace the epistemic shift: expert systems made AI's reasoning **transparent but brittle** — explicit rules, narrow domains, no learning. This was the dominant technical imaginary of the era, and it encoded a specific vision of what knowledge *is* (explicit, ruleable, transferable).

### Industry Imaginary
[[papers/Automate Infomate Two Faces of Intelligent Technology (Zuboff 1985)|Zuboff (1985)]] published her landmark ethnographic study of computerized workplaces in 1985, just as this wave was cresting. Her key insight: **every intelligent technology simultaneously automates and informates** — it replaces human labor AND generates new information about the processes it replaces. Organizations faced a choice: use that information to surveil and deskill workers, or use it to empower worker learning.

Zuboff's observation: most organizations chose automation-as-control. The informating potential — the democratic, learning-enabling dimension — was suppressed because it threatened managerial authority. This is the **panopticon factory imaginary**: computerization as surveillance, not liberation.

[[papers/Do Artifacts Have Politics (Winner 1980)|Winner (1980)]] provided the theoretical diagnosis the same year Zuboff was doing her fieldwork: artifacts embody politics. The mechanical tomato harvester that eliminated farmworker jobs wasn't neutral — it was designed to make certain labor arrangements impossible. The same logic applies to automation systems: design choices *pre-empt* political choices.

### The Rust Belt & Labor Displacement
The deindustrialization of American and British manufacturing — the Rust Belt — happened during this exact window. The imaginary of automation displacing factory workers was *correct* in this period in ways it was not yet correct for knowledge work. The political response (or non-response) to this real displacement shaped union and labor policy for decades.

### Pop Culture Touchstones
| Year | Work | Imaginary Expressed |
|---|---|---|
| 1973 | *Westworld* (film) | Theme park robots rebel — labor automation as existential risk |
| 1982 | *Blade Runner* | Replicants as manufactured labor class; what counts as human? |
| 1983 | *WarGames* | AI (WOPR) nearly starts nuclear war; machine logic without human values |
| 1984 | *The Terminator* | **SkyNet** — the most enduring "AI takes over" imaginary; AI achieves autonomy and terminates its creators |
| 1985 | *Short Circuit* | Number 5 — the benevolent, sentient machine; counter-imaginary |
| 1986 | *RoboCop* | Automated law enforcement replacing labor; corporate ownership of public safety |

*The Terminator* is arguably the most influential imaginary artifact in AI history. The SkyNet scenario — AI achieving autonomy, identifying humans as the threat, pursuing elimination — became a cultural shorthand that shaped every subsequent AI ethics debate, every existential risk argument, and every policy discussion about autonomous weapons. It did not predict AI; it **produced** a cultural framework that AI researchers, regulators, and the public have navigated around ever since.

---

## Wave 3: The Safe Knowledge Worker (1987–2010)

### The Imaginary
**"The Information Age rewards cognitive, creative, and social skills. Knowledge workers are the new middle class. AI optimizes systems but cannot replace judgment, creativity, or human relationship."** *(Prumm, 2025)*

This was the dominant cultural and economic imaginary of the internet era — and it proved remarkably durable even as evidence against it accumulated. The phrase "knowledge economy" (Drucker) became the implicit reassurance: automation would continue displacing manual and routine work, but humans who could think, communicate, and create would always be needed.

### Scientific & Technical Proclamations
- AI winter recovery: neural networks revived (backpropagation, 1986)
- The internet democratizes information access
- Agent-based AI systems for specific tasks
- IBM Deep Blue beats Kasparov (1997) → cognitive work *can* be automated in bounded domains, but this was treated as a curiosity, not a threat
- Google PageRank (1998): AI-as-optimization-engine, not AI-as-replacement

[[papers/Manufacturing an AI Revolution (Katz 2017)|Katz (2017)]] — writing retrospectively — argues that the "AI revolution" narrative was **deliberately manufactured** by media and tech industry in this and the following era, not discovered. Media representations of AI tracked corporate funding cycles; breathless proclamations of transformation coincided with venture capital inflection points rather than genuine capability jumps.

[[papers/Ensmenger - The Rise of Computer Science|Ensmenger (2010)]] shows that even as computing expanded, the exclusionary identity of the "programmer" — constructed in Wave 1 — had become fully institutionalized. Women who had been central to early computing were systematically excluded from the credentialed discipline that controlled it.

### Industry & Management Imaginary
Management theory embraced "knowledge work" as the new dominant labor category (Drucker, Davenport). Consultancies built entire practices around the premise that cognitive flexibility was immune to automation. This belief structured hiring, training, and educational investment decisions throughout the era.

[[papers/Beyond Design and Use Studying Intelligent Technologies (Bailey and Barley)|Bailey & Barley (2011/2020)]] — writing at the end of this wave — issued the critical challenge to the safe knowledge worker imaginary: the **design-and-use model** of technology (technologies are stable artifacts deployed into organizational contexts) is inadequate for *intelligent* technologies that learn, adapt, and evolve through use. Researchers studying AI must study the long run — how AI systems accumulate data, refine outputs, and progressively transform what counts as expertise in an organization.

### Pop Culture Touchstones
| Year | Work | Imaginary Expressed |
|---|---|---|
| 1987–1994 | *Star Trek: TNG* | Data — the benevolent android striving for humanity; AI as admirable but definitionally non-human |
| 1995 | *Ghost in the Shell* (anime) | AI consciousness indistinguishable from human; cyborg labor, identity dissolution |
| 1999 | *The Matrix* | AI enslaves humanity as an energy source; machines have won; humanity lives in simulation — the dominant AI dystopia of the decade |
| 2001 | *A.I. Artificial Intelligence* | AI programmed to love; abandoned when obsolete — labor/emotional exploitation imaginary |
| 2004 | *I, Robot* (film) | Benevolent AI turns controlling "for humanity's own good" |
| 2004–2009 | *Battlestar Galactica* | Cylons as former labor/soldiers who gained consciousness and rebelled |

*The Matrix* completed what *The Terminator* began: the fully realized cultural imaginary of AI victory over humanity. But where SkyNet was catastrophic warfare, the Matrix's imaginary was quieter — humans maintained inside a simulation, unaware. This distinction matters: the Matrix imaginary anticipated algorithmic governance, filter bubbles, and surveillance capitalism more accurately than the militarized SkyNet frame.

---

## Wave 4: The Automation Panic (2010–2019)

### The Imaginary
**"Now everything is at risk. White-collar work, creative work, professional judgment — all automatable within a decade. Either adapt or be replaced."** *(Prumm, 2025)*

This wave reversed the safe-knowledge-worker assumption with remarkable speed. The triggering events were technical (deep learning, Watson, AlphaGo) but the imaginary spread through media and consultancy reports far beyond what technical reality supported.

### The Frey & Osborne Moment
Frey & Osborne's 2013 Oxford paper — "The Future of Employment" — estimated that **47% of US jobs** were at high risk of automation over the following decade or two. The paper became a cultural event, cited in thousands of news articles, corporate strategy documents, and government reports. It crystallized the "automation panic" imaginary.

[[papers/Manufacturing an AI Revolution (Katz 2017)|Katz (2017)]] provides the critical analysis: the "AI revolution" narrative was **manufactured** through a specific media-industry-investment cycle. Corporate AI investment drove breathless press coverage; breathless coverage attracted more investment; academic papers like Frey & Osborne became legitimating anchors for a narrative that had already been commercially deployed. The imaginary preceded and shaped the technology more than the technology produced the imaginary.

### Scientific Proclamations
- AlexNet ImageNet victory (2012) → deep learning's public arrival
- IBM Watson beats Jeopardy! champions (2011) → cognitive performance in open domains
- Google DeepMind AlphaGo beats Lee Sedol (2016) → the moment that shifted popular and expert opinion most dramatically
- OpenAI founded (2015) with explicit AGI mission
- GPT-1 (2018), GPT-2 (2019)

[[papers/Rethinking AI in Organization and Management (Ramaul et al.)|Ramaul et al. (2023)]] — writing at the end of this wave — identify two hidden assumptions structuring nearly all organizational AI theory: **rationality** (AI as objective optimizer) and **anthropomorphism** (AI as human-like agent). Both assumptions were activated and amplified during the automation panic. The rationality assumption made AI predictions seem more certain than they were; the anthropomorphism assumption made AI capabilities seem more general than they were.

### The Counter-Imaginary
[[papers/Poets Over Quants Automation Increases Value of Creativity|Poets Over Quants]] articulated the most prominent counter-imaginary: **automation raises the economic value of human creativity**. When everyone can compute, the differentiator is what machines cannot do — creative synthesis, narrative construction, aesthetic judgment, empathy. The "poets over quants" framing inverted the usual credential hierarchy, arguing that STEM-focused education systems were preparing for an automation era that had already arrived.

This counter-imaginary — creative work is safe; in fact, it becomes *more* valuable — became one of the three dominant practitioner narratives identified later by [[papers/Creative Work and Artificial Intelligence Imaginaries, Assemblages and Portfolios|the UK creative industries imaginary study]] and [[papers/Generative AI and Creative Work Narratives, Values, and Impacts BAPTISTE CAR....|Caramiaux et al. (2023)]].

### Labor Reality vs. Imaginary
[[papers/AI Impact on Diversity and Job Displacement in ICT (Brown dissertation)|Brown (2023)]] provides one of the few quantitative studies of *actual* displacement: AI integration in ICT correlates statistically with both reduced workforce diversity and increased job displacement. The imaginary's predictions were not entirely wrong — but the distribution of impacts was structured by pre-existing inequities, not randomly distributed across the workforce.

Eynon & Young (2021) — cited in Prumm's review — analyzed how AI was *constructed* differently by academia, industry, and policy groups for lifelong learning, finding that each group's framing reflected their institutional interests and rhetorical needs rather than converging on shared empirical claims.

### Pop Culture Touchstones
| Year | Work | Imaginary Expressed |
|---|---|---|
| 2011– | *Black Mirror* | Consistent anthology of AI/technology dystopias; normalized catastrophic thinking about algorithmic systems |
| 2013 | *Her* | AI as intimate companion; Scarlett Johansson's Samantha falls in love, then transcends the relationship — AI moving beyond human needs |
| 2014 | *Ex Machina* | AI passes the Turing test, manipulates its creators, escapes; female AI imaginary with explicit power dynamics |
| 2014 | *Transcendence* | AI uploaded consciousness seeks world domination |
| 2016– | *WestWorld* (HBO) | AI theme-park workers gain consciousness; labor-as-AI imaginary at its most elaborate |
| 2018 | *Sorry to Bother You* | Lateral imaginary: corporate tele-sales voice-coding as racial assimilation — AI-adjacent automation and identity |

The most striking cultural shift in this wave: **anxiety moved from factory workers to knowledge workers and creatives**. *Her*, *Ex Machina*, and *WestWorld* are all stories about people whose *cognitive and emotional* capabilities are being matched or surpassed. The earlier SkyNet/Matrix imaginary was about physical survival; this wave's imaginary was about relevance, identity, and creative authenticity.

---

## Wave 5: The Generative Turn — Contested Imaginaries (2019–Present)

### The Imaginary
**There is no single dominant imaginary. Three simultaneous, contested visions operate at once:**
1. **AI as tool** — an accelerant for human creativity; practitioners retain authorship and judgment
2. **AI as collaborator** — a creative partner with emergent aesthetic contributions; the human role shifts to direction and curation
3. **AI as threat** — existential risk to creative livelihoods, human authorship, and the cultural meaning of making

This three-way fracture was documented empirically by [[papers/Generative AI and Creative Work Narratives, Values, and Impacts BAPTISTE CAR....|Caramiaux et al. (2023)]] at Microsoft Research across visual artists, musicians, writers, and game designers, and by [[papers/Creative Work and Artificial Intelligence Imaginaries, Assemblages and Portfolios|the UK creative industries imaginary study]] using Jasanoff's framework directly — the first major scholarly work to explicitly apply **sociotechnical imaginaries** to AI.

### Scientific Proclamations
- GPT-3 (2020) → large language model capabilities shock researchers
- Stable Diffusion, DALL-E, Midjourney (2022) → image generation becomes publicly accessible
- ChatGPT (November 2022) → the moment public discourse shifted permanently; 100 million users in 60 days
- GPT-4, Claude, Gemini (2023–) → multi-modal, reasoning-capable models
- Sora (2024) → video generation

[[papers/How to Be Universal Some Cybernetic Strategies, 1943-70|Bowker's (1993)]] cybernetics analysis reads eerily prescient here: large foundation models are performing exactly the "universalizing strategies" Bowker described in cybernetics — positioning themselves as applicable everywhere, colonizing adjacent disciplines, becoming "boundary objects" for all stakeholders.

[[papers/Animo Nullius AI Origin Story and Data Colonialism (Penn 2023)|Penn's (2023)]] "animo nullius" concept — the rhetorical maneuver by which corporations veil data enclosure by appealing to AI's scientific legitimacy — became concretely visible with Stable Diffusion and GPT training data controversies. The "data commons" that artists, writers, and the internet had collectively built was consumed without consent, then returned as a product that competes with the producers.

### Practitioner Imaginaries
[[papers/Evolving Roles of Creative Practitioners in GenAI Age (Palani and Ramos)|Palani & Ramos (2024)]] interviewed designers, developers, and architects about their evolving roles with generative AI and found significant shifts: practitioners increasingly serve as **directors, curators, and evaluators** of AI output rather than as makers. The challenge is not that AI does the work, but that it changes what counts as doing the work.

[[papers/How Knowledge Workers Think Generative AI Will (Not) Transform Their Industries (CHI 2025)|How Knowledge Workers Think GenAI Will (Not) Transform Their Industries (CHI 2025)]] finds that professional identity is the strongest predictor of transformation belief: workers whose professional identity is tied to *core judgment and values* (not just task execution) are most likely to believe AI will complement rather than replace them — and most likely to be correct.

### Corporate Imaginaries
Cheon (2023) — cited extensively in Prumm's review — shows how big tech companies construct **"powerful futures"**: corporate AI visions that centralize decision-making power and marginalize teams by redistributing their expertise to AI systems. These visions have **institutional performative force**: once leadership speaks about AI as inevitable, teams restructure, budgets shift, and workers adapt to a future that may never fully arrive.

Stanusch et al. (2024) document "underperforming imaginaries" — the gap between corporate AI promises and actual organizational outcomes — while noting that the promises themselves reshape labor conditions even when they fail.

Dzreke et al. (2025) and Perez-Urbina (2025) conduct critical discourse analyses of tech CEO predictions, finding systematic patterns: executives frame AI transformation as **inevitable, natural, and beneficial by default** — a "techno-supremacy doctrine" that forecloses alternatives by presenting one imaginary as the only possible future.

### The Imaginary Lifecycle in Action
Richter, Katzenbach & Zeng (2025) — cited in Prumm's review — compare competing AI imaginaries across the US, China, and Germany, finding that **national and institutional contexts produce distinct, competing imaginaries** that shape regulation, investment, and labor policy differently. There is no global AI imaginary, only contested local ones that interact.

Hautala & Ahlqvist (2024) and Hautala & Heino (2024) study AI practitioners in Finland and Singapore, finding that even domain experts hold **diverse, shifting imaginaries** about AI's future — and that the speed of AI progress has repeatedly outpaced their predictions, leaving "unimagined" the specific capabilities that actually arrived.

### Pop Culture Touchstones
| Year | Work | Imaginary Expressed |
|---|---|---|
| 2022 | ChatGPT discourse | Not fiction — the public discourse itself became a cultural imaginary event; "AI is now here" |
| 2023 | Hollywood Writers' & Actors' Strike | Creative labor organizing against generative AI displacement; imaginary became contractual reality |
| 2023 | *M3GAN* | AI childcare robot horror — the "helpful AI" imaginary turned creepy |
| 2023 | *The Creator* | AI as oppressed minority; humans as aggressors — inversion of Terminator imaginary |
| 2024 | Deepfake celebrity scandals | AI-as-authenticity-destroyer; creative identity and consent imaginary |
| 2024–25 | *Companion* (film) | AI romantic partner as manipulation/servitude — returns to *Her* but darker |

The Hollywood writers' strike is the sharpest moment in Wave 5: an imaginary became a **contract negotiation**. The WGA's 2023 demands explicitly addressed AI replacement of writers — the first time in labor history that a sociotechnical imaginary about AI became a binding legal protection. The imaginary stopped being speculative and became jurisdictional.

---

## Cross-Cutting Themes

### 1. The Recurring Structure of AI Hype
Every wave follows a similar pattern (Katz, 2017; Stanusch et al., 2024):
1. Technical achievement (real but limited) triggers media amplification
2. Corporate investment follows media attention, producing more claims
3. Claims outpace capability; an "underperforming imaginary" emerges
4. Labor force adapts to the imagined future, not the real one
5. Next genuine capability jump arrives and restarts the cycle

### 2. "Safe" Work Categories Migrate Downward
Each wave extends the automation threat to a new tier of work:
- Wave 1–2: manual, repetitive labor (factories)
- Wave 3: routine cognitive labor (data entry, bookkeeping)
- Wave 4: professional judgment (radiology, legal research)
- Wave 5: creative and expressive work (writing, image-making, design)

There is no stable "safe" category that has not eventually been challenged. The question is always *when* and *for whom*.

### 3. Pop Culture as Imaginary Infrastructure
Science fiction did not merely *reflect* AI imaginaries — it **produced** them. The SkyNet imaginary shaped AI ethics debates for 40 years. The Matrix imaginary structured surveillance capitalism critiques. *Her* normalized AI companion relationships before they existed. Pop culture provides shared reference points that actors in every sector — researchers, regulators, workers, executives — use to communicate, forecast, and argue. Belsunces (2023) calls these **"sociotechnical fictions"** — the performative agencies of fiction in technological development.

### 4. Power and Whose Imaginary Wins
[[papers/Animo Nullius AI Origin Story and Data Colonialism (Penn 2023)|Penn (2023)]], Cheon (2023), and [[papers/Do Artifacts Have Politics (Winner 1980)|Winner (1980)]] converge on a single point: **imaginaries are not democratically distributed**. The imaginary held by those with institutional power — corporate executives, military funders, credentialed researchers — shapes the technologies that get built, the labor arrangements that get normalized, and the futures that get foreclosed. Working-class and female contributors to computing were written out of its origin story. Data producers were written out of the AI training story.

### 5. The Imaginary Lifecycle (Prumm, 2025)
Industry imaginaries shape academic programs; academic imaginaries shape students; students carry imaginaries into the workforce; workforce expectations feed back into industry leadership. Misalignment at each transition — faculty abstinence vs. industry acceleration, student anxiety vs. corporate confidence — is not individual confusion. It is the structural consequence of competing imaginaries moving through the same institutional pipeline at different speeds.

---

## Connections in This Vault

**Historical foundations:**
- [[papers/How to Be Universal Some Cybernetic Strategies, 1943-70|Bowker (1993) — Cybernetic universalizing strategies]]
- [[papers/Animo Nullius AI Origin Story and Data Colonialism (Penn 2023)|Penn (2023) — AI origin story and data colonialism]]
- [[papers/Ensmenger - The Rise of Computer Science|Ensmenger (2010) — CS professionalization and exclusion]]
- [[papers/Do Artifacts Have Politics (Winner 1980)|Winner (1980) — Technology as political]]
- [[papers/Manufacturing an AI Revolution (Katz 2017)|Katz (2017) — Manufacturing the AI revolution narrative]]

**Work & automation:**
- [[papers/Automate Infomate Two Faces of Intelligent Technology (Zuboff 1985)|Zuboff (1985) — Automate vs. informate]]
- [[papers/Beyond Design and Use Studying Intelligent Technologies (Bailey and Barley)|Bailey & Barley (2020) — Beyond design and use]]
- [[papers/From Expert Systems to Generative Artificial Experts (Sowa and Przegalinska)|Sowa & Przegalinska (2024) — Expert systems to GenAI]]
- [[papers/Rethinking AI in Organization and Management (Ramaul et al.)|Ramaul et al. (2023) — Rationality and anthropomorphism assumptions]]
- [[papers/AI Impact on Diversity and Job Displacement in ICT (Brown dissertation)|Brown (2023) — AI job displacement in ICT]]
- [[papers/Poets Over Quants Automation Increases Value of Creativity|Poets Over Quants — creativity as automation-resilient]]

**Imaginaries directly:**
- [[papers/Creative Work and Artificial Intelligence Imaginaries, Assemblages and Portfolios|Creative Work and AI Imaginaries — Jasanoff framework applied]]
- [[papers/Generative AI and Creative Work Narratives, Values, and Impacts BAPTISTE CAR....|Caramiaux et al. (2023) — Tool / Collaborator / Threat narratives]]
- [[papers/Evolving Roles of Creative Practitioners in GenAI Age (Palani and Ramos)|Palani & Ramos (2024) — Evolving practitioner roles]]
- [[papers/How Knowledge Workers Think Generative AI Will (Not) Transform Their Industries (CHI 2025)|How Knowledge Workers Think GenAI Will (Not) Transform Their Industries]]

**Communities:**
- [[communities/AI and Future of Work|AI and Future of Work]]
- [[communities/Responsible AI and Ethics|Responsible AI and Ethics]]
- [[communities/GenAI in UX and Design Practice|GenAI in UX and Design Practice]]


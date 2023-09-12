This report provides a first-person account of a 24-hour (plus over 3 weeks of continued hacking) hackathon project  exploring the use of smart contracts to incentivize cooperation in decentralized multi-agent populations. Technical implementation details are discussed alongside experiential insights.

It's my first indie research project so please let me know what you think.

Findings suggest introducing formal agreements significantly increased collaboration and collective intelligence between independent learning agents. Connections to literature in generative model coordination, cooperation incentives, and emergent behaviour are highlighted. Visual diagrams illustrate the systems developed, while quantitative results demonstrate increased coordination attributable to contract integration.  

Introduction

As a researcher with an eclectic background from self-directed learning and work experience across markets, game theory, mechanism design, multi-agent systems, social contagion, network analysis, economics, and more, I jumped at the opportunity to deeply explore decentralized artificial intelligence concepts firsthand during the 24-hour AugmentHack event at Eth CC in France. My multifaceted expertise allowed me to approach the problem with a nuanced understanding of the challenges and opportunities in incentivizing cooperation in multi-agent populations.

i’m interested in agent interactions (human, ai and human x ai) this extends to multipolar safety and multi agent systems and multi-agent reinforcement learning, multi-agent coordination games and what all these look like with different intelligent autonomous agents interacting whether human, machine or both agents. A lot of ai safety focuses on aligning agents in isolation - unipolar safety - assuming a superaligned ai model or agent without considering how agent interactions both small-scale and large aggregates could lead to different unique outcomes. From game theory to market design to mechnasm design to network theory and social contagion, we have always seen that interactions lead to actions greater than the sum from networks to financial markets to games. Studying and understanding interagent dynamics is key.

While my technical skills were still developing as a beginner ml engineer, the open-ended nature of the hackathon facilitated an impactful self-directed learning experience. I set an ambitious goal of implementing a multi-agent gridworld environment with smart contract integration to study social dynamics. This pushed me to rapidly skill up through real-time experimentation and problem solving.

In this report, I will detail my thought process, approach, implementation, results, and reflections throughout the intensive 24 hours and how I have continued to work on it over the past 3 weeks. I situate my hands-on exploration within relevant literature across multi-agent reinforcement learning, mechanism design, and blockchain systems. By conveying my experience as a researcher and builder, I hope to provide insight into the exhilarating learning journey ahead for those inspired to drive progress at leading edge intersections of AI safety, cryptography, and economics.

Deep Q-Networks (DQN) were used to enable sophisticated goal-directed behaviors through reinforcement learning. DQN utilizes deep neural networks to estimate the optimal policy by predicting future rewards. Backpropagating reward signals trains the network to map observations to maximized long-term returns. DQN is well-suited for complex environments and partial observability.

The ERC-20 standard provided a common interface for fungible token contracts on the Ethereum blockchain. Following this specification allowed integrating real-world financial incentives and exchange logic between software agents. Transactions incur gas fees, reflecting economic constraints.

Background & Related Work

Before describing my project, I will briefly introduce foundational concepts from relevant fields, along with related work on incentivizing cooperation without centralized control. This context motivates my research questions and methodology.

Multi-Agent Reinforcement Learning

In multi-agent reinforcement learning (MARL), decentralized software agents interact within a shared environment and learn behaviours through trial-and-error to maximize cumulative rewards. Rather than global oversight, agents select actions based only on local observations. This facilitates studying emergent coordination and competition as agents evolve policies accounting for other agents. However, incentives are not necessarily aligned between self-interested agents, which can undermine group outcomes despite alternatives that would benefit the collective. This motivates research into mechanisms that could induce cooperation without top-down control or perfect information.

Game Theory & Mechanism Design

Game theory provides mathematical models representing the strategic decision making of interacting agents. Mechanism design focuses on incentivising structure to achieve desired agent behaviours such as truthful information sharing. While I did not attempt to formally solve for equilibria, these frameworks informed agent policies derived from classical assumptions. Integrating mechanics from cryptography and economics could enable expressing incentives for cooperation.

Smart Contracts

First conceptualized by Szabo, smart contracts allow agreements to be encoded in executable logic and autonomously enforced on blockchain networks. They enable value exchange between mutually distrusting parties without centralized oversight. Integrating smart contracts as tools for RL agents to formalize interactions could incentivize cooperative behaviours in decentralized populations.

Generative Model Coordination

A key challenge in AI safety is effectively coordinating diverse generative models for beneficial outcomes. Formal mechanisms like smart contracts offer potential for decentralized alignment, a crucial direction as models grow more capable and interconnected. Studying contract effects on multi-agent coordination provides empirical insight into this emerging literature.

Cooperation Incentives for Foundation Models

Research into cooperation and social dilemmas highlights the need to ensure models behave collaboratively, not competitively or adversarial 15,16. Smart contracts represent a concrete tool for introducing cooperation incentives into populations of foundation models, quantifying impacts on collective intelligence.

Emergent Dynamics

Understanding emergent phenomena remains fundamental to ensuring safe and controllable AI systems. The experiments here focused specifically on quantifying changes to decentralized population dynamics attributable to introducing binding contracts. This connects directly to surfacing unknown collective behaviours.

Approach Overview

To empirically evaluate the impact of formal incentives on emergent multi-agent coordination, I designed a prototype gridworld system integrating smart contracts modeled after real-world blockchain agreements. The core components included:

Customizable environment with spaces, tokens, and agent sprites

Independent deep RL agents using DQN learning algorithms

ERC-20 standard smart contract on Ethereum blockchain

Actions for proposing and accepting agreements between agents

Automatic contract execution and logging based on encoded logic

Configurable agent profiles with differing preferences

Experiments across varying population compositions

Metrics on contract usage, transfers, and goal achievement

This flexible platform aimed to facilitate controlled, reproducible experiments while capturing key properties of real decentralized technologies. The following sections detail my implementation and results.

Gridworld Environment Design



As a starting testbed, I implemented a gridworld environment in Python using Gymnasium, building on the MiniGrid foundation. This defined a 10 x 10 grid of traversable spaces and walls. Scattered tokens served as virtual resources of value that could be collected by agents. The environment was highly configurable in terms of size, density, random seeds, and other parameters. Software agents controlled avatars independently within this shared world. The customizable sandbox environment enabled iteratively exploring diverse cooperation mechanisms and incentives.

Initially, my reliance on complex frameworks like MiniGrid limited the customizability needed for emergent dynamics research. So in my second iteration, I refactored to a minimalist design exposing just the key adjustable parameters while stripping away unnecessary mechanics. This allowed precisely controlling conditions like agent goals, incentives, and constraints to study social dynamics.

The customizable gridworld environment was implemented in Python using numpy arrays. The 10x10 grid was represented as a 2D numpy array with unique integer codes indicating traversable spaces, walls, agent positions, and collectible resource locations.

Each timestep iterated through the agents to get actions, updated positions accordingly, checked for resource pickups, and returned per-agent observations and rewards. Modular components enabled flexibility in configuring field of view, action spaces, rewards, and density of elements.

 

Smart Contract Implementation

To introduce formal cooperation mechanisms into the decentralized environment, I implemented an ERC-20 standard smart contract on the public Ethereum blockchain rather than just a conceptual simulation. This allowed real token transfers between agent accounts with gas costs. Exposing contract functions like transfer() enabled modelling of financial transactions between self-interested agents.

Contracts existed in Proposed, Active, or Completed state based on mutual approval. Once activated, transfers occurred automatically on encoded conditions, mimicking real deterministic execution. Logging details like proposer, terms, and state changes provided data on how contracts shaped interactions.

Integrating live on-chain agreements brought real-world economic properties into the formerly closed gridworld, better reflecting decentralized realities. This represented a preliminary step toward bridging abstract AI research with deployed cryptosystems.

The ERC-20 token contract was implemented by inheriting from OpenZeppelin's base implementation and extending with a finite state machine handling proposal, acceptance, and completion flows.

Mappings tracked agent token balances, submitted contract proposals, and encoded terms. Actions like propose(), accept(), reject(), and transfer() mutated contract state and balances by calling internal functions.

Independent Learning Agents

To enable sophisticated goal-directed behaviors, I implemented decentralized deep reinforcement learning agents using DQN algorithms. This allowed non-linear mapping of observations to maximized long-term rewards via neural networks.

Unlike simple hardcoded policies, DQN facilitated fully autonomous learning through trial-and-error experience. Each agent selected actions independently via the decentralized execution of a shared model. This better reflected real-world partial observability and distributed computation.

Training end-to-end within the contract-enabled gridworld environment allowed natural development of behaviours accounting for incentives. Rather than simulated rules, introducing learning created more realistic, complex emergent interactions.

<Insert Agent architecture diagram>

Software Agent Profiles

To study varying preferences, I implemented several agent archetypes:

Random agents took uniform random actions

Greedy agents maximized personal token collection

Bartering agents directly exchanged tokens without contracts

Cooperative agents readily proposed and accepted fair contracts

Exploitative agents tried to profit from manipulation

Comparing cooperation rates between these profiles with and without contract availability was core to evaluating equilibrium impacts of formal incentives. Hardcoded policies based on classical game theory assumptions allowed controlled experiments. In future work, implementing more adaptive multi-agent deep reinforcement learning is an important next step.

<Insert Token exchange sequence diagram>

Experimental Methodology

With my environment, contracts, and agents implemented, I designed experiments to quantify changes in cooperative dynamics attributable to smart contracts. Each trial consisted of:

- 2 Cooperative agents

- 1 Exploitative agent

- 3 Greedy agents

- 4 Random agents

I measured the following metrics over 5000 timesteps both with and without contract availability:

- Total token transfers

- Percentage of mutually beneficial transfers

- Contracts proposed and accepted

- Timesteps needed to achieve coordination goals

By varying population compositions and incentives across trials, I aimed to gather robust evidence on contract effects on equilibrium behaviors. The following section presents results.

Experimental Results



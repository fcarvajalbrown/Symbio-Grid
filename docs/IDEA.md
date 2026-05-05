## 3. The "Social Norm" Epidemiological Simulator
While LLMs can predict text, they struggle to simulate the emergent behavior of thousands of individuals. Researchers are currently using agent-based models to simulate how **social novelties** and norms (like the adoption of a new health behavior) emerge through simple agent interactions and "urn models" (Suda et al., 2024).

*   **The Project:** Create a simulation of a town where each "Person Agent" has a set of internal **Belief-Desire-Intention (BDI)** rules. For example: `IF (Neighbor_Infected > 2) AND (Mask_Available) THEN (Wear_Mask)`.
*   **The "Old School" Brain:** **Cellular Automata** or **GABM (Generalised Agent Based Model)**. These models allow you to see how a small change in individual logic (a "bias") leads to a massive shift in community health.
*   **Why it’s Zenodo-worthy:** Public health researchers need "white-box" simulations. By publishing your **Agent Logic Parameters** and the resulting **Emergence Data**, you contribute to the science of "Social Physics."




To take the simple logic of *The Game of Life* (1970) and give it a 2026 "noble" twist, you can move from simple survival rules to **Evolutionary Rule-Space Agents**. 

Recent 2026 research from the Wolfram Community and others has shifted away from static rules toward **Evolvable AI (eAI)**—where the "physics" of the grid itself evolves based on the agents' success.

### The Project: "Symbio-Grid: An Evolutionary Mycelial Automaton"

Instead of just black and white cells, you create a simulation of the **"Wood Wide Web"**—the symbiotic relationship between trees and underground fungal networks (mycelium). This is highly publishable on Zenodo because it maps to **Eco-Informatics** and **Sustainable Systems**.

---

### 1. The Setup (Beyond the Grid)
*   **The Agents:** 
    *   **Plant Agents:** Stationary, produce "Carbon" (Resource A) but need "Phosphorus" (Resource B).
    *   **Fungi Agents:** Mobile (expanding hyphae), find "Phosphorus" in the soil but need "Carbon."
*   **The "Old School" Brain:** No LLMs. Each agent has a **BDI (Belief-Desire-Intention)** profile.
    *   **Belief:** "I have 5 units of Carbon."
    *   **Desire:** "I need Phosphorus to survive."
    *   **Intention:** "Trade Carbon with the nearest Fungi Agent."

### 2. The 2026 "Modern Twist": Evolving Rule-Tables
In the original *Game of Life*, the rule "Stay alive if 2 or 3 neighbors" is fixed. In your project, the **rules are genetic**.
*   Each agent carries a tiny **Symbolic Rule-Table** (a bit-string). 
*   **Example Rule:** `IF Neighbor_Count == X AND Resource_Level < Y THEN Mutate_State`.
*   When agents successfully trade resources and "reproduce," their rule-tables undergo **Stochastic Mutation** (Wolfram, 2026). 
*   **The Goal:** Watch as the grid evolves from a chaotic mess into a highly organized, cooperative "bio-economy" where trees and fungi thrive together.

### 3. Why this is "Zenodo-Noble"
Publishing a repo that just "runs a game" isn't enough for Zenodo. To make it a scientific contribution, you publish the **Emergent Rule-Set Library**:
1.  **FAIR Data:** You run 10,000 simulations and export the "DNA" (Rule-Tables) of the most stable, resilient ecosystems.
2.  **The Social Impact:** This isn't just a game; it’s a model for **Circular Economies**. It demonstrates how decentralized agents (without a central "government") can reach a state of equilibrium through local trade rules.
3.  **Climate Science:** You can add a "Climate Shock" variable (e.g., pH level changes) to see which symbolic rules allow the ecosystem to survive a 2°C warming scenario.

---

### 4. Comparison: 1970 vs. 2026

| Feature | Conway's Game of Life (1970) | Your Symbio-Grid (2026) |
| :--- | :--- | :--- |
| **Logic** | Hardcoded (If 3, Live) | **Adaptive** (BDI + Rule Evolution) |
| **Resources** | None (Binary) | **Multi-Resource** (Carbon/Phosphorus) |
| **Goal** | Visual Patterns | **Systemic Resilience** |
| **AI Type** | Basic Cellular Automata | **Symbolic Multi-Agent System (MAS)** |

### How to Start (The "No-LLM" Tech Stack)
*   **Engine:** [Mesa](https://mesa.readthedocs.io/) (Python framework for Agent-Based Modeling). It handles the grid and the agent loops beautifully.
*   **Logic:** Use a simple **Genetic Algorithm** to mutate the rule-tables.
*   **Visualization:** Use **Pygame** or **Matplotlib** for that classic retro-grid look, but with heatmaps for resource concentration.

**Sample Rule Logic (Pythonic Pseudo-code):**
```python
class FungiAgent(Agent):
    def step(self):
        # 1. Sense: Check neighbor resources
        targets = self.get_neighbors(radius=1)
        # 2. Think: Use the evolved rule-table (The 'Old School' Brain)
        decision = self.rule_table.query(self.current_state)
        # 3. Act: Trade or Expand
        if decision == "TRADE":
            self.execute_trade(targets)
```

**Zenodo Title Idea:** 
> *"A Library of Evolutionary Stable Rule-Tables for Fungal-Plant Symbiosis in Decentralized Multi-Agent Systems"*

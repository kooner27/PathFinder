***
# Pathfinding Algorithms on Video Game Maps

This project implements **A\***, **Bidirectional A\*** (Bi-A\*), and **MM (Meet in the Middle)** algorithms to solve pathfinding problems on grid-based video game maps. It explores the efficiency and performance of heuristic-guided search algorithms.

***


## Overview

The implemented algorithms solve pathfinding problems in a grid environment where:

- Movements include cardinal directions (cost = 1.0) and diagonals (cost = 1.5).
- Problems consist of a video game map, a start location, and a goal location.

The algorithms calculate the **solution cost** and the **number of nodes expanded**, generating scatter plots for performance analysis.

---

## Features

1. **Algorithms Implemented**:

   - **A\***: Uses Octile distance as a heuristic.
   - **Bi-A\***: Expands nodes from both start and goal, meeting in the middle.
   - **MM**: A bidirectional search algorithm with optimal stopping conditions.

2. **Visualization**:

   - Generates scatter plots comparing node expansions:
     - MM vs. A\*
     - MM vs. Bi-A\*

3. **Test Instances**:

   - Includes 30 predefined test cases for consistency in results.

4. **Performance Metrics**:
   - Solution cost.
   - Nodes expanded during the search.
   - Scatter plots for comparative analysis.

---

## How to Run

1. **Setup Environment**:

   - Install Python 3.
   - Create a virtual environment (optional):
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

2. **Run the Program**:
   - Execute the main script with test instances:
     ```bash
     python3 main.py --testinstances
     ```
   - Generate scatter plots:
     ```bash
     python3 main.py --testinstances --plots
     ```

---

## Results

The project generates two scatter plots:

- **Nodes Expanded**: Comparing MM with A* and Bi-A*.
- Observations and analyses are included below.

---

## Insights and Analysis

1. **Effect of Heuristics**:

   - In general, the use of a heuristic function **decreases** the number of nodes the algorithm needs to expand to find a solution.

2. **Running Time vs. Expansions**:

   - The running time decreases **exactly in the same proportion** as the number of expansions decreases.
   - This is because the algorithms differ only in their cost functions, and the time complexity of calculating the cost function is unaffected by the heuristic.

3. **MM vs. Bi-A\***:

   - MM tends to perform **fewer expansions** than Bi-A\*.

4. **Effectiveness of Heuristic-Guided Bidirectional Algorithms**:

   - In this specific experiment, the heuristic-guided bidirectional algorithms **did not substantially reduce the number of expansions** compared to other methods.

5. **Scatter Plot Comparison (A\* vs. MM)**:
   - A* and MM differ in how they prioritize the heuristic (h) and cost functions. A* relies heavily on the heuristic, as it assigns equal weight to g and h.
   - MM’s cost function, `max(f, 2g)`, restricts the search from extending too far in one direction, leading to a broader exploration.
   - This causes MM to expand more nodes than A* in cases where the heuristic is highly reliable, as A* focuses more directly on the optimal path.

---

## File Structure

- `main.py`: Runs the experiments.
- `bibfs_algo.py`: Bidirectional A\* implementation.
- `dijkstra_algo.py`: Baseline Dijkstra’s algorithm.
- `mm.py`: Meet in the Middle algorithm.
- `requirements.txt`: Python dependencies.
- `test-instances/`: Test cases and maps.
- `nodes_expanded_mm_astar.png`: Scatter plot for MM vs. A\*.
- `nodes_expanded_mm_biastar.png`: Scatter plot for MM vs. Bi-A\*.

---

## Dependencies

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## Additional Resources

Dr. Holte, from the University of Alberta, where I studied, was instrumental in developing this algorithm, which guarantees that forward and backward searches meet in the middle, as outlined in their 2016 paper:

## [Bidirectional Search That Is Guaranteed to Meet in the Middle (2016)](https://webdocs.cs.ualberta.ca/~holte/Publications/MM-AAAI2016.pdf)

# Maze Solver

## Introduction

Maze Solver is a Python-based program that uses various search algorithms to find paths in mazes. It supports Breadth-First Search (BFS), Depth-First Search (DFS), and Greedy Best-First Search (GBFS).

## Features

- Multiple search algorithms: BFS, DFS, GBFS
- Visualization of the maze-solving process
- Customizable maze environments
- Error handling for common issues (e.g., multiple agents, no goals, etc.)

## Getting Started

### Prerequisites

- Python 3.11

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/maze-solver.git
    ```

2. Navigate to the project directory:

    ```bash
    cd maze-solver
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the program:

    ```bash
    python main.py
    ```

2. Choose a search algorithm (BFS, DFS, GBFS).
3. Watch the maze-solving process, and view the visualization.

## Possible Errors and Handling

The Maze Solver program incorporates error handling to address common issues that may arise during maze solving. Below are possible errors and how they are handled:

1. **NoAgentFound:**
   - *Description:* This error occurs when there is no agent (starting point) in the maze.
   - *Handling:* The program raises a `NoAgentFound` exception with an informative message. Users should ensure that the maze includes a single agent.

2. **NoGoalFound:**
   - *Description:* Raised when there are no goals in the maze.
   - *Handling:* The program raises a `NoGoalFound` exception with a default message. Users should verify that the maze includes at least one goal.

3. **MultipleAgentsFound:**
   - *Description:* Occurs when there is more than one agent in the maze.
   - *Handling:* The program raises a `MultipleAgentsFound` exception with a descriptive message. Users need to correct the maze configuration to have a single agent.

4. **NoPathFound:**
   - *Description:* Raised when a search algorithm cannot find a path to the goal.
   - *Handling:* The program raises a `NoPathFound` exception. Users may need to modify the maze to ensure a valid path exists.

5. **FuntionNotFound:**
   - *Description:* Raised when an unsupported or unknown search algorithm is specified.
   - *Handling:* The program raises a `FuntionNotFound` exception with a default message. Users should use one of the supported search algorithms: BFS, DFS, or GBFS.

Feel free to refer to the [Errors.py](Errors.py) file for detailed information about each custom error class.


## Dependencies

- NumPy
- Matplotlib

## Contributing

Contributions are welcome! Feel free to submit issues, feature requests, or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact Information

For inquiries, please contact [m.muhayodin2005@gmail.com](mailto:m.muhayodin2005@gmail.com).

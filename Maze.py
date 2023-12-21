import copy
import time

import numpy as np
from matplotlib import pyplot as plt, animation

import Errors


class MainFuntion:

    @staticmethod
    def getPositionInitially(Env):
        """
        Gets the initial position of Agent in Array of maze
        :param Env: Maze array
        :return: AgentInitialPosition, Number_Of_Goal, Positions_Of_Goal  # Return Values
        :raises: Errors.MultipleAgentsFound: If there are more than one agent
        :raises: Errors.NoGoalFound: If there is no Goal in the Environment
        :raises: Errors.NoAgentFound: If there is no agent in the Environment
        """
        # The following funtion is used to get the Position of Agent in the array
        AgentInitialPosition = np.where(np.array(Env) == 2)  # Get array with Position of Agent
        if len(AgentInitialPosition[0]) > 1:  # Checking if there are more than one agent in Array
            raise Errors.MultipleAgentsFound  # More than one agent in Array
        Number_Of_Goal = len(np.where(np.array(Env) == 3)[0])  # Checking the Number of Goals
        if Number_Of_Goal == 0:  # If there are no goals in array
            raise Errors.NoGoalFound()  # Raising Custom Error from Errors.py
        Positions_Of_Goal = []  # Empty set to store Positions of Goals
        for i in range(Number_Of_Goal):  # Looping for the number of times as Goals
            Positions_Of_Goal.append(
                [np.where(np.array(Env) == 3)[0][i], np.where(np.array(Env) == 3)[1][i]])  # Appending to Goal Set
        try:
            AgentInitialPosition = [AgentInitialPosition[0][0], AgentInitialPosition[1][0]]  # Trying to Agent
        except IndexError:
            raise Errors.NoAgentFound()  # Raise Error if there is no agent
        return AgentInitialPosition, Number_Of_Goal, Positions_Of_Goal  # Return Values

    def __init__(self, Environment, verbose=1):  # Initialization Funtion for class
        """
        :raises Errors.FuntionNotFound: If funtion is not found
        :raises Errors.EnvironmentInError: If all the rows are not of Equal Length
        :param Environment: Maze Array
        :param verbose: Printing Settings
        """
        self.verbose = verbose  # Getting Value For Verbose
        self.out = None  # Initializing out
        try:
            (self.InitialPosition, self.num_goal,
             self.Position_Of_Goals) = self.getPositionInitially(np.array(Environment))  # Getting All Values Required
        except ValueError:
            raise Errors.EnvironmentInError("The rows in the Environment are heterogeneous")
        self.Environment = Environment  # Setting the Environment

        # Printing Info:
        if self.verbose == 0:  # If verbose is 0
            print("Starting....")
        elif self.verbose == 1:  # If verbose is 1
            Time = time.localtime()
            print(f"Starting at {Time[3]}:{Time[4]}:{Time[5]}; {Time[2]}-{Time[1]}-{Time[0]}")  # Time
        elif self.verbose == 3:  # If verbose is 3
            Time = time.localtime()
            print(f"Starting at {Time[3]}:{Time[4]}:{Time[5]}; {Time[2]}-{Time[1]}-{Time[0]}")  # Time
            print("\n\n\n")
            print(Environment)  # Maze
            print("\n\n\n")
            print("Initial Position Of Agent: " + str(self.InitialPosition))  # InitialPosition
            print("Number of Goals: " + str(self.num_goal))  # Number of Goals
            print("Positions of Goals: " + str(self.Position_Of_Goals))  # Positions of Goals
            print("\n\n\n")
        else:
            print("Verbose Error")  # Some Error

    def bfs(self):
        """
        Breadth-First Search (BFS) is a versatile graph traversal algorithm that systematically explores tree or
        graph structures level by level, starting from the initial node and moving outward. Utilizing a queue-based
        approach, BFS ensures that all nodes at a particular level are visited before progressing to the next level.
        Widely applied in network routing, social network analysis, and web crawling, BFS guarantees the shortest
        path in unweighted graphs, demonstrating its efficacy in scenarios where optimality and efficiency are
        paramount. With a time complexity of (O(V + E)) in a graph with (V) vertices and (E) edges,
        BFS's simplicity and completeness make it a fundamental tool in computer science and beyond.
        :raises: Errors.NoPathFound: If no path is found
        """
        Environment = np.array(self.Environment)
        numberOfGoal = self.num_goal
        initialPosition = self.InitialPosition
        Frontier = []  # Initializing Frontier Set
        History = []  # Initializing History Set
        Goals = []  # Initializing Goals Set
        Frames = []  # Initializing Frames set
        Env = copy.deepcopy(Environment)  # Making Deepcopy of Array IMP
        Frames.append(np.array(copy.deepcopy(Env)))  # Appending to Frames set for representation of start of Maze
        Frontier.append(initialPosition)  # Appending Initial Position to Frontier
        while numberOfGoal != 0:  # While there are more goals
            try:
                Now = Frontier[0]  # Now value is the first Value from the frontier
            except IndexError:
                raise Errors.NoPathFound()
            # Checking if the current Value is Goal
            if Environment[Now[0]][Now[1]] == 3:  # 3 is Goal
                Goals.append(Now)  # Appending to Goal Set
                numberOfGoal -= 1  # Reducing number of remaining goals

            History.append(Now)  # Appending to History
            Env[Now[0]][Now[1]] = 4  # Changing Current Index in Frames to 4
            Frames.append(np.array(copy.deepcopy(Env)))  # Appending ↑ this to frames
            if numberOfGoal == 0:  # if Number of Goals is Zero break the loop
                break
            Frontier = Frontier[1:]  # Removing first value from the Frontier
            # Checking Right
            if Now[1] + 1 < Environment.shape[1]:
                Right = [Now[0], Now[1] + 1]
                if Environment[Right[0]][Right[1]] != 0:
                    if Right not in History:
                        Frontier.append(Right)

            # Checking Left
            if Now[1] - 1 >= 0:
                Left = [Now[0], Now[1] - 1]
                if Environment[Left[0]][Left[1]] != 0:
                    if Left not in History:
                        Frontier.append(Left)

            # Checking Below
            if Now[0] + 1 < Environment.shape[0]:
                Below = [Now[0] + 1, Now[1]]
                if Environment[Below[0]][Below[1]] != 0:
                    if Below not in History:
                        Frontier.append(Below)

            # Checking Above
            if Now[0] - 1 > 0:
                Above = [Now[0] - 1, Now[1]]
                if Environment[Above[0]][Above[1]] != 0:
                    if Above not in History:
                        Frontier.append(Above)

        self.out = Goals, Frames, History

    def printing_out(self):
        """
        The funtion is used to print the steps taken by the Algorithm
        :return: Animation Funtion
        """
        if self.verbose > 0:  # Checking the Verbose
            print("Animating Steps Taken By The Algorithm")
        _, frames, _ = self.out
        # Getting Data
        fig, ax = plt.subplots()  # Plotting
        im = ax.imshow(frames[0], interpolation='none')  # Showing Image

        def update(i):  # Updating Funtion
            im.set_array(frames[i])
            return im,

        ani = animation.FuncAnimation(fig, update, frames=len(frames), interval=300, blit=True)
        plt.show()  # Showing Plot
        return ani

    @staticmethod
    def printP(Environment, Path):
        """
        This funtion is used to Animate a specific path that can be given by param Path
        :param Environment: Maze array
        :param Path: Path taken
        :return: ani
        """
        frames = []  # Initializing Empty Frames Set
        Path = Path[::-1]  # Reversing Path Set
        for i in Path:  # Looping
            Environment[i[0]][i[1]] = 4  # Setting the new Value as 4
            frames.append(copy.deepcopy(Environment))  # Appending to Frame
        fig, ax = plt.subplots()  # Plotting
        im = ax.imshow(frames[0], interpolation='none')  # Showing Funtion

        def update(ix):  # Update Funtion
            im.set_array(frames[ix])
            return im,

        ani = animation.FuncAnimation(fig, update, frames=len(frames), interval=300, blit=True)
        plt.show()  # Show
        return ani

    def get_best_path(self):
        """
        This funtion is deprecated
        :return: Cleaned Path
        """
        if self.verbose > 0:  # Printing Funtion
            print("Attempting To Get The Best Path From The History")
        _, _, history = self.out  # Returning Funtion Call
        start = [history[0]]
        path = [history[-1]]
        BackH = history[::-1]  # Reverse of History
        for i in path:
            N = self.get_neighbors(i)  # Get Neighbors
            if self.verbose > 1:  # Checking Verbose
                print(f"Path : {path}", f"BackH: {BackH}")
                print(f"Neighbors: {N}")
            BackH.pop(BackH.index(i))  # Popping Done
            for n in N:
                if n in BackH and n not in path:
                    path.append(n)  # Appending to Path
            if path[-1] in start:
                break
        if self.verbose > 1:  # Printing
            print(BackH)
        if self.verbose > 1:
            print(f"We have removed {len(history) - len(path)} Steps.")

        return path

    @staticmethod
    def get_neighbors(position):  # Getting Neighbours
        """
        Funtion is used to get the neighbouring indxes of an index
        :param position: Index whose position is required
        :return: [Right, Left, Below, Above]
        """
        # Helper function to get neighboring positions
        return [
            [position[0], position[1] + 1],  # Right
            [position[0], position[1] - 1],  # Left
            [position[0] + 1, position[1]],  # Below
            [position[0] - 1, position[1]]  # Above
        ]

    def dfs(self):
        """Depth-First Search (DFS) is a graph traversal algorithm commonly used to explore and analyze structures
        like maze. The algorithm starts from a designated node, known as the "root" in trees,
        and systematically explores as deeply as possible along each branch before backtracking. DFS can be
        implemented using a stack or recursion, maintaining a record of visited nodes to avoid revisiting them. Its
        applications range from maze solving to identifying connected components in undirected graphs and performing
        topological sorting in directed acyclic graphs. While DFS is not always optimal for finding the shortest
        path, its simplicity and efficiency make it a fundamental algorithm with a time complexity of O(V + E),
        where V is the number of vertices and E is the number of edges in the graph.

        :raises: NoPathFound: If the frontier is empty with the goal not found
        :returns: Goals, Frames, History
        """
        Environment = np.array(self.Environment)
        initialPosition = self.InitialPosition
        numberOfGoal = self.num_goal
        Frontier = []  # Initializing Frontier
        History = []  # Initializing History
        Goals = []  # Initializing Goals
        Frames = []  # Initializing Frames
        Env = copy.deepcopy(Environment)  # Deep-copying Environment
        Frames.append(np.array(copy.deepcopy(Env)))  # Appending Frames
        Frontier.append(initialPosition)  # Appending Frontier
        while numberOfGoal != 0:  # Unless the Goals are zero
            try:  # Check if the Frontier is Null
                Now = Frontier[-1]
            except IndexError:
                raise Errors.NoPathFound()  # If the Frontier is Zero but Goals not zero
            # print("Environment\n" + str(Env))
            if Environment[Now[0]][Now[1]] == 3:
                Goals.append(Now)
                numberOfGoal -= 1

            History.append(Now)
            Env[Now[0]][Now[1]] = 4
            Frames.append(np.array(copy.deepcopy(Env)))
            if numberOfGoal == 0:
                break  # Breaking
            Frontier = Frontier[:-1]
            # Checking Right
            if Now[1] + 1 < Environment.shape[1]:
                Right = [Now[0], Now[1] + 1]
                if Environment[Right[0]][Right[1]] != 0:
                    if Right not in History:
                        Frontier.append(Right)

            # Checking Left
            if Now[1] - 1 >= 0:
                Left = [Now[0], Now[1] - 1]
                if Environment[Left[0]][Left[1]] != 0:
                    if Left not in History:
                        Frontier.append(Left)

            # Checking Below
            if Now[0] + 1 < Environment.shape[0]:
                Below = [Now[0] + 1, Now[1]]
                if Environment[Below[0]][Below[1]] != 0:
                    if Below not in History:
                        Frontier.append(Below)

            # Checking Above
            if Now[0] - 1 > 0:
                Above = [Now[0] - 1, Now[1]]
                if Environment[Above[0]][Above[1]] != 0:
                    if Above not in History:
                        Frontier.append(Above)

        self.out = Goals, Frames, History

    def gbfs(self):
        """
        Greedy Best-First Search (GBFS) is a graph traversal algorithm used for pathfinding, particularly in
        scenarios where a heuristic can guide the search. Unlike traditional search algorithms, GBFS prioritizes
        nodes based on heuristic evaluations. The algorithm maintains a priority queue, selecting nodes with the
        lowest heuristic values, indicating their proximity to the goal. GBFS continues to expand nodes until the
        goal is reached or the entire space is explored. While GBFS may not guarantee optimality, its efficiency
        relies on the quality of the heuristic function. When the heuristic accurately estimates the true cost,
        GBFS can quickly find solutions. Notably applied in route planning, robotics, and games, GBFS is part of the
        family of informed search algorithms, offering an effective approach to navigating large state spaces.

        :raises: NoPathFound: If the frontier is empty with the goal not found
        :return: Positions_of_goals, Frames, History
        """
        initialPosition = self.InitialPosition
        Positions_of_goals = self.Position_Of_Goals
        Environment = np.array(self.Environment)
        Frontier = [[initialPosition][0]]
        History = []
        Num_Goals = len(Positions_of_goals)
        Frames = []
        Env = copy.deepcopy(Environment)
        while Num_Goals != 0:
            best = float('inf')
            choice = []
            for i in Frontier:
                for p in Positions_of_goals:
                    if abs(p[0] - i[0]) + abs(p[1] - i[1]) < best:
                        best = abs(p[0] - i[0]) + abs(p[1] - i[1])
                        choice = i
            # Checking If Choice Is Goal
            try:
                Env[choice[0]][choice[1]] = 4
            except IndexError:
                raise Errors.NoPathFound()
            Frames.append(copy.deepcopy(Env))
            if Environment[choice[0]][choice[1]] == 3:
                Num_Goals -= 1
            Frontier.pop(Frontier.index(choice))

            # Up
            if choice[0] - 1 >= 0:
                if Environment[choice[0] - 1][choice[1]] != 0:
                    if choice not in History:
                        Frontier.append([(choice[0] - 1), (choice[1])])
            # Left
            if choice[1] - 1 >= 0:
                if Environment[choice[0]][choice[1] - 1] != 0:
                    if choice not in History:
                        Frontier.append([(choice[0]), (choice[1] - 1)])
            # Below
            if choice[0] + 1 <= (Environment.shape[0] - 1):
                if Environment[choice[0] + 1][choice[1]] != 0:
                    if choice not in History:
                        Frontier.append([(choice[0] + 1), (choice[1])])

            if choice[1] + 1 <= (Environment.shape[1] - 1):
                if Environment[choice[0]][choice[1] + 1] != 0:
                    if choice not in History:
                        Frontier.append([(choice[0]), (choice[1] + 1)])

            History.append(choice)
            # break
        self.out = Positions_of_goals, Frames, History
        return

    def giveBestOut(self):
        self.gbfs()
        Goals_G, Frames_G, History_G = self.out
        self.bfs()
        Goals_B, Frames_B, History_B = self.out
        self.dfs()
        Goals_D, Frames_D, History_D = self.out
        print(f"G: {len(History_G)}, B: {len(History_B)}, D: {len(History_D)}")
        if len(History_G) > len(History_D) < len(History_B):
            if self.verbose != 0:
                print("DFS CHOSEN")
            return Goals_D, Frames_D, History_D
        elif len(History_D) > len(History_G) < len(History_B):
            if self.verbose != 0:
                print("GBFS CHOSEN")
            return Goals_G, Frames_G, History_G
        elif len(History_G) > len(History_B) < len(History_D):
            if self.verbose != 0:
                print("BFS CHOSEN")
            return Goals_B, Frames_B, History_B

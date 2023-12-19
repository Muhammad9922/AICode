import copy
import time

import numpy as np
from matplotlib import pyplot as plt, animation

import Errors


class ClassicFunctions:

    @staticmethod
    def getPositionInitially(Env):
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

    def __init__(self, Environment, module: str = 'dfs', verbose=1):  # Initialization Funtion for class
        self.verbose = verbose  # Getting Value For Verbose
        self.module = module  # Getting the Module or Funtion
        self.out = None  # Initializing out
        (self.InitialPosition, self.num_goal,
         self.Position_Of_Goals) = self.getPositionInitially(np.array(Environment))  # Getting All Values Required
        self.Environment = Environment  # Setting the Environment

        # Printing Info:
        if self.verbose == 0:
            print("Starting....")
        elif self.verbose == 1:
            Time = time.localtime()
            print(f"Starting at {Time[3]}:{Time[4]}:{Time[5]}; {Time[2]}-{Time[1]}-{Time[0]}")
            print(f"Mode: {module}")
        elif self.verbose == 3:
            Time = time.localtime()
            print(f"Starting at {Time[3]}:{Time[4]}:{Time[5]}; {Time[2]}-{Time[1]}-{Time[0]}")
            print(f"Mode: {module}")
            print("\n\n\n")
            print(Environment)
            print("\n\n\n")
            print("Initial Position Of Agent: " + str(self.InitialPosition))
            print("Number of Goals: " + str(self.num_goal))
            print("Positions of Goals: " + str(self.Position_Of_Goals))
            print("\n\n\n")
        else:
            print("Verbose Error")

        # Setting Algorithm
        if self.module.lower() == 'bfs':
            self.out = self.bfs(np.array(self.Environment), self.InitialPosition, self.num_goal)
        elif self.module.lower() == 'dfs':
            self.out = self.dfs(np.array(self.Environment), self.InitialPosition, self.num_goal)
        elif self.module.lower() == 'gbfs':
            if not self.Position_Of_Goals:
                raise ValueError("Position of Goals Not Defined")  # Position of Goals is Required for this
            self.out = self.gbfs(np.array(self.Environment), self.InitialPosition, self.Position_Of_Goals)
        else:
            raise Errors.FuntionNotFound  # If Funtion has an error

    def returner(self):
        """
        Returns all the values for the sake of further use
        :return: Tuple of data Values as Goals, Frames, History
        :rtype: tuple
        """
        return self.out

    @staticmethod
    def bfs(Environment: np.array, initialPosition: list, numberOfGoal: int = 0):
        """
        Breadth First Search has the policy of First Come First Go. This essentially check most of the places in the
        environment
        :param Environment: Maze in form of list or array
        :param initialPosition: Initial Position of Agent
        :param numberOfGoal: Numbers of Goals in the environment
        :return: Tuple of data Values as Goals, Frames, History
        """
        Frontier = []  # Initializing Frontier Set
        History = []  # Initializing History Set
        Goals = []  # Initializing Goals Set
        Frames = []  # Initializing Frames set
        Env = copy.deepcopy(Environment)  # Making Deepcopy of Array IMP
        Frames.append(np.array(copy.deepcopy(Env)))  # Appending to Frames set for representation of start of Maze
        Frontier.append(initialPosition)  # Appending Initial Position to Frontier
        while numberOfGoal != 0:  # While there are more goals
            Now = Frontier[0]  # Now value is the first Value from the frontier

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

        return Goals, Frames, History

    def printing_out(self):
        if self.verbose > 0:        # Checking if verbose allows printing
            print("Animating Steps Taken By The Algorithm")
        _, frames, _ = self.returner()      # Getting Frames
        fig, ax = plt.subplots()
        im = ax.imshow(frames[0], interpolation='none')     # Showing

        def update(i):                                      # Updating
            im.set_array(frames[i])                         # Setting new array
            return im,

        ani = animation.FuncAnimation(fig, update, frames=len(frames), interval=300, blit=True)
        plt.show()
        return ani

    @staticmethod
    def printP(Environment, Path):
        frames = []                                     # Initializing Frames
        Path = Path[::-1]                               # Reversing Path
        for i in Path:                                  # Looping Through Path
            Environment[i[0]][i[1]] = 4                 # Updating Environment
            frames.append(copy.deepcopy(Environment))   # Adding to frames
        fig, ax = plt.subplots()
        im = ax.imshow(frames[0], interpolation='none')

        def update(ix):                                 # Updating
            im.set_array(frames[ix])                    # Setting new array
            return im,

        ani = animation.FuncAnimation(fig, update, frames=len(frames), interval=300, blit=True)
        plt.show()
        return ani

    def get_best_path(self):
        if self.verbose > 0:                            # If verbose allows
            print("Attempting To Get The Best Path From The History")
        _, _, history = self.out
        start = [history[0]]                            # Start Position
        path = [history[-1]]                            # Last History To Path
        BackH = history[::-1]                           # Reverse history → BackH
        for i in path:
            N = self.get_neighbors(i)
            if self.verbose > 1:
                print(f"Path : {path}", f"BackH: {BackH}")
                print(f"Neighbors: {N}")
            BackH.pop(BackH.index(i))
            for n in N:
                if n in BackH and n not in path:
                    path.append(n)
            if path[-1] in start:
                break
        if self.verbose > 1:
            print(BackH)
        if self.verbose > 1:
            print(f"We have removed {len(history) - len(path)} Steps.")

        return path

    @staticmethod
    def get_neighbors(position):
        # Helper function to get neighboring positions
        return [
            [position[0], position[1] + 1],  # Right
            [position[0], position[1] - 1],  # Left
            [position[0] + 1, position[1]],  # Below
            [position[0] - 1, position[1]]  # Above
        ]

    @staticmethod
    def dfs(Environment: np.array, initialPosition: list, numberOfGoal: int = 0):
        Frontier = []
        History = []
        Goals = []
        Frames = []
        Env = copy.deepcopy(Environment)
        Frames.append(np.array(copy.deepcopy(Env)))
        Frontier.append(initialPosition)
        while numberOfGoal != 0:
            try:
                Now = Frontier[-1]
            except IndexError:
                raise Errors.NoPathFound()
            # print("Environment\n" + str(Env))
            if Environment[Now[0]][Now[1]] == 3:
                Goals.append(Now)
                numberOfGoal -= 1

            History.append(Now)
            Env[Now[0]][Now[1]] = 4
            Frames.append(np.array(copy.deepcopy(Env)))
            if numberOfGoal == 0:
                break
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

        return Goals, Frames, History

    @staticmethod
    def gbfs(Environment: np.array, initialPosition: list, Positions_of_goals):
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
            Env[choice[0]][choice[1]] = 4
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
        return Positions_of_goals, Frames, History

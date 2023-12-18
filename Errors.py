class NoAgentFound(Exception):
    """
    No Agent In Environment
    """

    def __init__(self, message = "No Agent Found"):
        super().__init__(message)
        assert isinstance(message, str)
        self.message = message


class NoGoalFound(Exception):
    """
    No Goal In Environment
    """

    def __init__(self, message= "NoGoalFound"):
        super().__init__(message)
        assert isinstance(message, str)
        self.message = message


class MultipleAgentsFound(Exception):
    """
    Multiple Agents In Environment
    """

    def __init__(self, message = "More than one Agents in the Array"):
        super().__init__(message)
        assert isinstance(message, str)
        self.message = message


class NoPathFound(Exception):
    """
    There is no path in the given Maze
    """
    pass


class FuntionNotFound(Exception):
    """
    The function being called is either not available or there is an error in the instance
    """
    def __init__(self, message="Algorithm Not Found"):
        super().__init__(message)
        assert isinstance(message, str)
        self.message = message

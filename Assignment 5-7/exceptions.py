class InvalidNumberOfParametersException(Exception):
    def __init__(self, message=""):
        """

        :param message: class str
        """
        self._message = "Invalid number of parameters! " + message

    def __str__(self):
        return self._message


class InvalidIdException(Exception):
    def __init__(self, message=""):
        self._message = "Invalid id! " + message

    def __str__(self):
        return self._message


class RepositoryException(Exception):
    """
    Exception class for book repository errors
    """
    def __init__(self, message=""):
        """
        Constructor for repository exception class
        message - A string representing the exception message
        """
        self._message = message

    def __str__(self):
        return self._message

class InvalidCommandException(Exception):
    """
    Exception for invalid command
    Valid commands: ...
    """
    def __init__(self, message=""):
        """
        Constructor for the invalid command class
        :param message: string representing the exception message
        """
        self._message = "Invalid command!"

    def __str__(self):
        return self._message
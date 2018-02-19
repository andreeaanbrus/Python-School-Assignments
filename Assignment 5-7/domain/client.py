class Client:
    class_counter = 0
    def __init__(self, id=0, name=""):
        self._id = id
        self._name = name

    def setId(self, value):
        self._id = value

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def setName(self, value):
        self._name = value

    def __str__(self):
        return "ID: " + str(self._id) + " | Name:" + self._name

    def update(self, other):
        """
        Updates a client : name (ID must not be changed)
        :param other: class Client
        :return: -
        """
        self.setName(other.getName())

    def __eq__(self, other):
        if self._name == other.getName() and self._id == other.getId():
            return True
        return False

    @staticmethod
    def fromLine(line):
        params = line.split(";")
        return Client(int(params[0]), params[1])

    @staticmethod
    def toLine(client):
        return str(client.getId()) + ';' + client.getName() + '\n'
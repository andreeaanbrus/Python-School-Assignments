class Settings:
    def __init__(self):
        self._repository = ""

    def getRepository(self):
        with open("settings.txt", "r") as f:
            line = f.readline()
        line = line.strip()
        line = line.split(" ")
        self._repository = line[2]
        return self._repository

    def setRepository(self, other):
        self._repository = other

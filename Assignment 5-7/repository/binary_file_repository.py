import pickle

from repository.repository import Repository

class BinaryFileRepository(Repository):
    def __init__(self, fileName):
        Repository.__init__(self)
        self._fileName = fileName
        self.readAllFromFile()

    def writeAllToFile(self):
        with open(self._fileName, "wb") as f:
            pickle.dump(self._data, f)

    def readAllFromFile(self):
        with open(self._fileName, "rb") as f:
            self._data = pickle.load(f)

    def add(self, other):
        Repository.add(self, other)
        self.writeAllToFile()

    def remove(self, id):
        Repository.remove(self, id)
        self.writeAllToFile()

    def update(self, id, object):
        Repository.update(self, id, object)
        self.writeAllToFile()


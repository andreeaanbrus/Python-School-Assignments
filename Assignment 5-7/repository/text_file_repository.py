from repository.repository import Repository


class TextFileRepository(Repository):
    def __init__(self, fileName, fromLine, toLine):
        self._fromLine = fromLine
        self._toLine = toLine
        Repository.__init__(self)
        self._fileName = fileName
        self.readAllFromFile()

    def readAllFromFile(self):
        with open(self._fileName, "r") as f:
            for line in f.readlines():
                line = line.strip()
                if len(line) > 0:
                    o = self._fromLine(line)
                    self._data.append(o)

    def writeAllToFile(self):
        with open(self._fileName, "w") as f:
            try:
                for elem in self._data:
                    line = self._toLine(elem)
                    f.write(line + '\n')
                #f.close()
            except Exception as e:
                print("An error occured -" + str(e))

    def appendToFile(self, object):
        with open(self._fileName, "a") as f:
            line = self._toLine(object)
            f.write(line)

    def add(self, other):
        Repository.add(self, other)
        self.appendToFile(other)

    def remove(self, id):
        Repository.remove(self, id)
        self.writeAllToFile()

    def update(self, id, object):
        Repository.update(self, id, object)
        self.writeAllToFile()

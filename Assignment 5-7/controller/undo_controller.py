class UndoController:
    def __init__(self):
        self._history = []
        self._index = -1

    def recordOperation(self, cascadeOp):
        """
        Record the operation for undo/redo

        :return: -
        """
        #self._history = self._history[:(self._index - 1)]

        if self._index != len(self._history) - 1:
            self._history = self._history[:(self._index + 1)]
        self._history.append(cascadeOp)
        self._index += 1


    def undo(self):
        """
        Undo the last operation
        :return: True if undo was successful
                False otherwise
        """
        if self._index == -1:
            return False
        self._history[self._index].undo()
        self._index -= 1
        return True

    def redo(self):
        """
        Redo the last operation
        :return: True id redo was successful
                False otherwise
        """
        if self._index == len(self._history) - 1:
            return False
        self._index += 1
        self._history[self._index].redo()
        return True

class FunctionCall():
    def __init__(self, functionRef, *parameters):
        self._functionRef = functionRef
        self._parameters = parameters

    def call(self):
        self._functionRef(*self._parameters)

    # def __str__(self):
    #     return str(self._functionRef) + str(self._parameters)

class Operation:
    def __init__(self, functionDo, functionUndo):
        self._functionDo = functionDo
        self._functionUndo = functionUndo

    def undo(self):
       # print(self._functionUndo)
        self._functionUndo.call()

    def redo(self):
       # print(self._functionDo)
        self._functionDo.call()


class CascadeOperation:
    def __init__(self, op=None):
        self._operations = []
        if op is not None:
            self.add(op)

    def add(self, op):
        self._operations.append(op)

    def undo(self):
        for i in range(len(self._operations) - 1, -1, -1):
            self._operations[i].undo()

    def redo(self):
        for i in range(len(self._operations) - 1, -1, -1):
            self._operations[i].redo()

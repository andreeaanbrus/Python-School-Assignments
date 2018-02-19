import copy


class GnomeSort:
    """
    worst case performance: O(n^2)
    best case performance: O(n)
    average performance: O(n^2)
    """
    def __init__(self, list, key, reverse):
        self._list = list
        self._key = key
        self._reverse = reverse

    def getList(self):
        return self._list

    def setList(self, other):
        self._list = other

    def getKey(self):
        return self._key

    def setKey(self, other):
        self._key = other

    def getReverse(self):
        return self._reverse

    def setReverse(self, other):
        self._reverse = other

    def sort(self):
        if self._key == None:
            self.setKey(lambda x:x)
        if self._reverse == False:
            pos = 0
            while (pos < len(self._list)):
                if pos == 0 or self._key(self._list[pos]) >= self._key(self._list[pos - 1]):
                    pos += 1
                else:
                    aux = copy.deepcopy(self._list[pos])
                    self._list[pos] = self._list[pos - 1]
                    self._list[pos - 1] = aux
                    pos -= 1
        if self._reverse == True:
            pos = 0
            while (pos < len(self._list)):
                if pos == 0 or self._key(self._list[pos]) <= self._key(self._list[pos - 1]):
                    pos += 1
                else:
                    aux = copy.deepcopy(self._list[pos])
                    self._list[pos] = self._list[pos - 1]
                    self._list[pos - 1] = aux
                    pos -= 1
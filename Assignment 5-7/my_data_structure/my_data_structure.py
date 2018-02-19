import copy

from my_data_structure.sorting_algorithm import GnomeSort


class MyList:
    def __init__(self):
        self._list = []

    def __iter__(self):
        return iter(self._list)

    def __next__(self, ob):
        return next(ob)

    def __setitem__(self, key, value):
        self._list[key] = value

    def __getitem__(self, item):
        return self._list[item]

    def __delitem__(self, key):
        del self._list[key]

    def __len__(self):
        return len(self._list)

    def append(self, value):
        self._list.append(value)

    def remove(self, value):
        self._list.remove(value)

    def pop(self, index):
        self._list.pop(index)

    def __str__(self):
        return str(self._list)

    def __eq__(self, other):
        for i in range(0, len(self._list)):
            if self._list[i] != other[i]:
                return False
        return True

    def sort(self, key=None, reverse=False):
        sort = GnomeSort(self._list, key, reverse)
        sort.sort()

    def filter(self, key=None, value=""):
        if key == None:
            return self._list
        if value == None:
            return self._list
        res = MyList()
        for i in range(0, len(self._list)):
            if(key(self._list[i]) == value):
                res.append(self._list[i])
        return res

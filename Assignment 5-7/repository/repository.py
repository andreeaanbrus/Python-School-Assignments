from exceptions import RepositoryException
from my_data_structure.my_data_structure import MyList


class Repository:
    def __init__(self):
        self._data = MyList()

    def add(self, object):
        """
        Add an object to the repository
        """
        self._data.append(object)

    def remove(self, object):
        """
        Removes an object from the repository
        """
        #del self._data[id]
        #self._data.pop(id)
        self._data.remove(object)

    def update(self, id, object):
        """
        Updates the book at the position id with a new book
        :param id: the given position
        :param object: the new object
        :return: -
        """
        self._data[id].update(object)

    def __len__(self):
        """

        :return: The size of the list
        """
        return len(self._data)

    def getAll(self):
        """

        :return: ALl the elements in the list
        """
        return self._data[:]  # deepcopy

    def get(self, index):
        if index < 0 or index >= len(self._data):
            raise RepositoryException("Invalid element position")
        return self._data[index]

class Book:

    def __init__(self, id=0, title='', description='', author=''):

        self._title = title
        self._description = description
        self._author = author
        self._id = id


    def setId(self, value):
        self._id = value

    def getId(self):
        return self._id

    def getTitle(self):
        return self._title

    def setTitle(self, value):
        self._title = value

    def getDescription(self):
        return self._description

    def setDescription(self, value):
        self._description = value

    def getAuthor(self):
        return self._author

    def setAuthor(self, value):
        self._author = value

    def __str__(self):
        return 'ID: ' + str(
            self._id) + ' | Title: ' + self._title + ' | Description: ' + self._description + ' | Author: ' + self._author

    def update(self, other):
        """
        Updates a book - title, description and author (the id must not be changed)
        :param other: class book
        :return:-
        """
        self.setTitle(other.getTitle())
        self.setDescription(other.getDescription())
        self.setAuthor(other.getAuthor())

    def __eq__(self, other):
        if self._author == other.getAuthor() and self._title == other.getTitle() and self._description == other.getDescription() \
                and self._id == self.getId():
            return True
        return False

    @staticmethod
    def fromLine(line):
        params = line.split(";")
        return Book(int(params[0]), params[1], params[2], params[3])

    @staticmethod
    def toLine(book):
        return str(book.getId()) + ';' + book.getTitle() + ';' + book.getDescription() + ';' + book.getAuthor() + '\n'


import copy
import re

from controller.undo_controller import FunctionCall, Operation, CascadeOperation
from domain.book import Book
from exceptions import InvalidIdException


class BookController():
    def __init__(self, repository, undoController, rentalController):
        self._bookRepo = repository
        self._undoController = undoController
        self._rentalController = rentalController

    def addBook(self, id, title, description, author ,recordForUndo = True):
        """
        Adds a new book
        :param book: class Book
        :return: book - for undo/redo
        """
        if self.checkId(id) == False:
            raise InvalidIdException
        book = Book(id, title, description, author)
        self._bookRepo.add(book)

        if recordForUndo == True:
            undo = FunctionCall(self.removeBook, id, False)
            redo = FunctionCall(self.addBook, id, title, description, author, False)
            operation = Operation(redo, undo)
            self._undoController.recordOperation(operation)

        return book

    def removeBook(self, id, recordForUndo = True):
        """
        Removes the book with a given id
        :param id: the id of the book that will be removed
        :return: the removed book if book was removed
                Exception otherwise
        """
        book = self.findBookByBookId(id)
        index = self.findIndexInRepo(id)
        cascadeOp = CascadeOperation()

        if recordForUndo:
            list = self._rentalController.removeRentalByBookId(id)
            for i in range(len(list)-1, -1, -1):
                undo_casc = FunctionCall(self._rentalController.addRental, list[i].getId(), list[i].getBookId(),
                                         list[i].getClientId(), list[i].getRentedDate(), list[i].getDueDate(),
                                         list[i].getReturnedDate(), False)
                redo_casc = FunctionCall(self._rentalController.removeRental, list[i].getId(), False)
                op = Operation(redo_casc, undo_casc)
                cascadeOp.add(op)

            undo = FunctionCall(self.addBook, book.getId(), book.getTitle(), book.getDescription(), book.getAuthor(),
                                False)
            redo = FunctionCall(self.removeBook, book.getId(), False)
            operation = Operation(redo, undo)
            cascadeOp.add(operation)
            self._undoController.recordOperation(cascadeOp)


        self._bookRepo.remove(book)
        return book

    def updateBook(self, id, title, description, author, recordForUndo = True):
        """
        Updates the book with the given id with a new book
        :param id: int
        :param title: the new title
        :param description: the new description
        :param author: the new author
        :return:the book before it was updated
        """
        okId = False
        for i in self._bookRepo.getAll():
            if id == i.getId():
                okId = True
        if not okId:
            raise InvalidIdException
        lastBook = copy.deepcopy(self.findBookByBookId(id))
        index = self.findIndexInRepo(id)
        book = Book(id, title, description, author)

        if recordForUndo == True:
            undo = FunctionCall(self.updateBook, id, lastBook.getTitle(), lastBook.getDescription(), lastBook.getAuthor(), False)
            redo = FunctionCall(self.updateBook, id, title, description, author, False)
            operation = Operation(redo, undo)
            self._undoController.recordOperation(operation)
        self._bookRepo.update(index, book)
        return lastBook

    def getBooks(self):
        """
        Gets all the rentals from the repository (for printing)
        :return: all rentals
        """
        return self._bookRepo.getAll()

    def searchBooks(self, params):
        """
        finds all the books by a given substring
        :param params: str, the given substring
        :return:    list of the matches
        """
        list = []
        token = str(params[0])
        for i in self._bookRepo.getAll():
            if re.search(token, i.getTitle(), re.IGNORECASE) or re.search(token, i.getAuthor(), re.IGNORECASE) or re.search(token, str(i.getId()), re.IGNORECASE)or re.search(token, i.getDescription(), re.IGNORECASE):
                list.append(i)
        return list

    def findIndexInRepo(self, bookId):
        """

        :param bookId: the given position
        :return: the index in the repository of the book
        """
        index = 0
        for i in self._bookRepo.getAll():
            if i.getId() != bookId:
                index += 1
            else:
                return index
        raise InvalidIdException

    def findBookByIndex(self, index):
        """

        :param index: the given index
        :return: the object found at that index
        """
        return self._bookRepo.getAll()[index]

    def findBookByBookId(self, id):
        """

        :param id: the given id
        :return: The object with a given id
        """
        for i in self._bookRepo.getAll():
            if i.getId() == id:
                return i

    def checkId(self, id):
        """
        Checks if there exists another object with that id
        :param id: the given id, int
        :return: True, False
        """
        for i in self._bookRepo.getAll():
            if i.getId() == id:
                return False
        return True

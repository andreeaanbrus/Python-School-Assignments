import copy
import datetime

from controller.undo_controller import FunctionCall, Operation, CascadeOperation
from domain.rental import Rental
from exceptions import InvalidIdException
from my_data_structure.my_data_structure import MyList


class RentalController():
    def __init__(self, rentalRepo, bookRepo, clientRepo, undoController):
        self._rentalRepo = rentalRepo
        self._bookRepo = bookRepo
        self._clientRepo = clientRepo
        self._undoController = undoController

    def addRental(self, id, bookId, clientId, rentalDate=datetime.timedelta(0), dueDate=datetime.timedelta(0),
                  returnedDate="", recordForUndo=True):
        """
        Adds a new rent to repository
        :param rent: rent class
        :return: rental
        """
        if self.checkId(id) == False:
            raise InvalidIdException
        if rentalDate == datetime.timedelta(0):
            rentalDate = datetime.datetime.now().date()
        if dueDate == datetime.timedelta(0):
            dueDate = rentalDate + datetime.timedelta(days=10)
        rental = self.validation(id, bookId, clientId, rentalDate, dueDate, returnedDate)
        self._rentalRepo.add(rental)
        if recordForUndo == True:
            undo = FunctionCall(self.removeRental, id, False)
            redo = FunctionCall(self.addRental, id, bookId, clientId, rentalDate, dueDate, returnedDate, False)
            operation = Operation(redo, undo)
            self._undoController.recordOperation(operation)

        return rental

    def removeRental(self, id, recordForUndo=True):

        rental = self.getRentalById(id)
        oldRental = copy.deepcopy(rental)
        if recordForUndo:
            undo = FunctionCall(self.addRental, oldRental.getId(), oldRental.getBookId(), oldRental.getClientId(),
                                oldRental.getRentedDate(), oldRental.getDueDate(), oldRental.getReturnedDate(), False)
            redo = FunctionCall(self.removeRental, oldRental.getId(), False)
            operation = Operation(redo, undo)
            self._undoController.recordOperation(operation)

        self._rentalRepo.remove(rental)

        return oldRental

    def removeRentalByBookId(self, bookId):
        """
        If a book gets deleted, all the rentals with the bookId in them should be deleted
        :param bookId: int
        :return: the list of deleted rentals
        """

        list = []
        for i in self._rentalRepo.getAll():
            if i.getBookId() == bookId:
                rental = copy.deepcopy(i)
                list.append(rental)

        i = 0
        while i < len(self._rentalRepo.getAll()):
            if self._rentalRepo.get(i).getBookId() == bookId:
                self._rentalRepo.remove(self._rentalRepo.get(i))
            else:
                i += 1

        return list

    def removeRentalByClientId(self, clientId):
        """
        If a clients gets deleted, all the rentals with the clientId in them should be deleted
        :param clientId: int
        :return: the list of rentals that were deleted
        """
        list = []
        for i in self._rentalRepo.getAll():
            if i.getClientId() == clientId:
                rental = copy.deepcopy(i)
                list.append(rental)
        i = 0
        while i < len(self._rentalRepo.getAll()):
            if self._rentalRepo.get(i).getClientId() == clientId:
                self._rentalRepo.remove(self._rentalRepo.get(i))
            else:
                i += 1
        return list

    def getRentals(self):
        """
        :return: gets all books from repo (for print)
        """
        return self._rentalRepo.getAll()

    def getRental(self, id):
        """

        :return: rental with certain id
        """
        return self._rentalRepo.get(id)

    def updateRental(self, id, bookId, clientId, rentedDate, dueDate, returnedDate, recordForUndo=True):
        """
        Updates the rental with a given id with the given data
        """
        rental = Rental(id, bookId, clientId, rentedDate, dueDate, returnedDate)
        oldRental = copy.deepcopy(self.getRentalById(id))
        index = self.getIndexById(oldRental.getId())
        self._rentalRepo.update(index, rental)
        if recordForUndo == True:
            undo = FunctionCall(self.updateRental, oldRental.getId(), oldRental.getBookId(), oldRental.getClientId(),
                                oldRental.getRentedDate(),
                                oldRental.getDueDate(), oldRental.getReturnedDate(), False)
            redo = FunctionCall(self.updateRental, id, bookId, clientId, rentedDate, dueDate, returnedDate, False)
            operation = Operation(redo, undo)
            self._undoController.recordOperation(operation)

        return oldRental

    def returnBook(self, id):
        """
        Sets the returned-date to the current date
        :param id: the id of the rental
        :return:the unmodified rental
        """
        rental = self.getActiveRentalByBookId(id)
        index = self.getIndexById(rental.getId())
        if not rental:
            raise InvalidIdException()
        returnedDate = datetime.datetime.now().date()
        self.updateRental(rental.getId(), rental.getBookId(), rental.getClientId(), rental.getRentedDate(),
                          rental.getDueDate(), returnedDate)
        self._rentalRepo.update(index, rental)

    def validation(self, id, bookId, clientId, rentalDate, dueDate, returnedDate):
        if self.rentalValidation(bookId, clientId):
            return Rental(id, bookId, clientId, rentalDate, dueDate, returnedDate)

    def rentalValidation(self, bookId, clientId):
        """
        Checks if the parameters are ok for a new rental
        :param bookId: the book id int
        :param clientId: the client id int
        :return:True
        """
        if self.inRepoClient(clientId) == False:
            raise InvalidIdException("Wrong client id!")

        if self.inRepoBook(bookId) == False:
            raise InvalidIdException("Wrong book id!")

        for i in self._rentalRepo.getAll():
            # if i.getBookId() == bookId and i.getReturnedDate() == datetime.timedelta(0):
            if i.getBookId() == bookId and i.getReturnedDate() == "":
                raise InvalidIdException("Book is rented!")

        ok = False
        for i in self._bookRepo.getAll():
            if i.getId() == bookId:
                ok = True
        for j in self._clientRepo.getAll():
            if j.getId() == clientId:
                ok = True
        if not ok:
            raise InvalidIdException()
        else:
            return True

    # STATISTICS

    def mostRentedBooks(self):
        """
        :return: the list of most rented books
        bookCounter[i] =  i-book id, the number of rentals of i, i-title
        """
        bookCounter = MyList()
        books = self._bookRepo.getAll()
        rentals = self._rentalRepo.getAll()

        for i in books:
            bookCounter.append(BookRental(i.getId(), i.getTitle(), 0))

        for i in rentals:
            for j in bookCounter:
                if i.getBookId() == j.getBookId():
                    j.incrementRentalCount()

        bookCounter.sort(key=lambda x: x.getRentalCount(), reverse=True)

        return bookCounter

    def mostRentedAuthors(self):
        """

        :return: the list of the most rented authors
        """
        authorCounter = MyList()
        books = self._bookRepo.getAll()
        rentals = self._rentalRepo.getAll()

        for i in books:
            authorCounter.append(AuthorRental(i.getId(), i.getAuthor(), 0))

        for i in rentals:
            for j in authorCounter:
                if i.getBookId() == j.getBookId():
                    j.incrementRentalCount()
        for i in range(0, len(authorCounter) - 1):
            for j in range(i + 1, len(authorCounter)):
                if authorCounter[i].getBookAuthor() == authorCounter[j].getBookAuthor():
                    authorCounter[i].addRentalCount(authorCounter[j].getRentalCount())
                    authorCounter[j] = AuthorRental(0, "", 0)
        i = 0
        while i < len(authorCounter):
            if authorCounter[i].getBookAuthor() == "":
                authorCounter.remove(authorCounter[i])
            else:
                i += 1

        authorCounter.sort(key=lambda x: x.getRentalCount(), reverse=True)

        result = []
        for i in authorCounter:
            result.append(i)
        return result

    def lateRentals(self):

        res = MyList()
        rentals = self._rentalRepo.getAll()
        today = datetime.datetime.now().date()
        for i in rentals:
            if i.getDueDate() < today and i.getReturnedDate() == "":
                bookId = i.getBookId()
                numberOfDays = today - i.getDueDate()

                title = self.getBookTitleByBookId(bookId)
                res.append(LateRental(title, numberOfDays.days))
                res.sort(key=lambda x: x.getNumberOfDays(), reverse=True)
        return res

    def mostActiveClients(self):
        """
        :return: The statistic of the most active clients, in descending order of the number of days that they rented books
        """
        res = MyList()
        rentals = self._rentalRepo.getAll()
        for i in rentals:
            numberOfDays = datetime.timedelta(0)
            rentalsByClient = self.getAllRentalsByClientId(i.getClientId())
            for j in rentalsByClient:
                numberOfDays += j.getDueDate() - j.getRentedDate()
            res.append(ClientActivity(self.clientNameById(i.getClientId()), numberOfDays.days))
        """
        Eliminate the clients with the same name
        """
        res.sort(key=lambda x: x.getClient())
        for i in range(0, len(res) - 1):
            if res[i].getClient() == res[i + 1].getClient():
                res[i].setClient("")
        i = 0
        while i < len(res):
            while res[i].getClient() == "":
                res.remove(res[i])
            else:
                i += 1
        res.sort(key=lambda x: x.getNumberOfDays(), reverse=True)
        return res

    # UTILS

    def getRentalByBookId(self, bookId):
        """

        :param bookId: the book id, int
        :return: The rental found with the book id, Rental type
                False, if it doesn;t exist
        """
        for i in self._rentalRepo.getAll():
            if i.getBookId() == bookId:
                return i
        return False

    def clientNameById(self, id):
        """

        :param id: the cient's id from the rental repo, int
        :return: the name of the client, str
        """
        for i in self._clientRepo.getAll():
            if i.getId() == id:
                return i.getName()

    def getActiveRentalByBookId(self, bookId):
        """
        Returns rental by given book id - checks if book is returned
        :param bookId: int
        :return: rental
        """
        for i in self._rentalRepo.getAll():
            if bookId == i.getBookId() and i.getReturnedDate() == "":
                return i
        return False

    def getBookTitleByBookId(self, bookId):
        """
        Returns the book title by the book id
        :param bookId: int
        :return: book title, string
                raise exception if id doesn't exist in books
        """
        for i in self._bookRepo.getAll():
            if i.getId() == bookId:
                return i.getTitle()
        raise InvalidIdException()

    def getAllRentalsByClientId(self, id):
        """

        :param id: the client id, int
        :return: all rentals which have the client id - id
        """
        res = []
        rentals = self._rentalRepo.getAll()
        for i in rentals:
            if i.getClientId() == id:
                res.append(i)
        return res

    def getRentalById(self, id):
        for i in self._rentalRepo.getAll():
            if i.getId() == id:
                return i

    def lastElemFromRepo(self):
        """
        :return: the number of the last element from the repo, or 0 if the list is empty
        """
        counter = 0
        for i in self._rentalRepo.getAll():
            counter += 1
        return counter

    def inRepoClient(self, clientId):
        for i in self._clientRepo.getAll():
            if i.getId() == clientId:
                return True
        return False

    def inRepoBook(self, bookId):
        for i in self._bookRepo.getAll():
            if i.getId() == bookId:
                return True
        return False

    def checkId(self, id):
        """
        Checks if there exists another object with that id
        :param id: the given id, int
        :return: True, False
        """
        for i in self._rentalRepo.getAll():
            if i.getId() == id:
                return False
        return True

    def getIndexById(self, id):
        """

        :param id: the rental id
        :return: the index of the rental in repo
        """
        for i in range(0, len(self._rentalRepo.getAll())):
            if self._rentalRepo.getAll()[i].getId() == id:
                return i
        return False


class AuthorRental():
    def __init__(self, bookId, bookAuthor, rentalCount):
        self._bookId = bookId
        self._bookAuthor = bookAuthor
        self._rentalCount = rentalCount

    def getBookId(self):
        return self._bookId

    def getBookAuthor(self):
        return self._bookAuthor

    def getRentalCount(self):
        return self._rentalCount

    def incrementRentalCount(self):
        self._rentalCount += 1

    def addRentalCount(self, value):
        self._rentalCount += value

    def __str__(self):
        return str("The author " + self._bookAuthor + " was rented " + str(self._rentalCount) + " times")

    def __eq__(self, other):
        if self._rentalCount == other.getRentalCount() and self._bookId == other.getBookId() and self._bookAuthor == other.getBookAuthor():
            return True
        return False


class BookRental():
    def __init__(self, bookId: object, bookTitle: object, rentalCount: object) -> object:
        self._bookTitle = bookTitle
        self._rentalCount = rentalCount
        self._bookId = bookId

    def getBookId(self):
        return self._bookId

    def getBookTitle(self):
        return self._bookTitle

    def getRentalCount(self):
        return self._rentalCount

    def incrementRentalCount(self):
        self._rentalCount += 1

    def __str__(self):
        return str("The book " + self._bookTitle + " was rented " + str(self._rentalCount) + " times")

    def __eq__(self, other):
        if self._bookId == other.getBookId() and self._bookTitle == other.getBookTitle() and self._rentalCount == other.getRentalCount():
            return True
        return False


class LateRental():
    def __init__(self, bookTitle, numberOfDays):
        self._bookTitle = bookTitle
        self._numberOfDays = numberOfDays

    def setBookTitle(self, value):
        self._bookTitle = value

    def getBookTitle(self):
        return self._bookTitle()

    def getNumberOfDays(self):
        return self._numberOfDays

    def setNumberOfDays(self, value):
        self._numberOfDays = value

    def __str__(self):
        return str("The book '" + self._bookTitle + "' was not returned on time. Number of days of delay: " + str(
            self._numberOfDays))

    def __eq__(self, other):
        if self._numberOfDays == other.getNumberOfDays and self._bookTitle == other.getBookTitle():
            return True
        return False


class ClientActivity():
    def __init__(self, client, numberOfDays):
        self._client = client
        self._numberOfDays = numberOfDays

    def setClient(self, value):
        self._client = value

    def getClient(self):
        return self._client

    def setNumberOfDays(self, value):
        self._numberOfDays = value

    def getNumberOfDays(self):
        return self._numberOfDays

    def __str__(self):
        return str("The client " + str(self._client) + " rented books for " + str(self._numberOfDays) + " days")

    def __eq__(self, other):
        if self._numberOfDays == other.getNumberOfDays() and self._client == other.getClient():
            return True
        return False

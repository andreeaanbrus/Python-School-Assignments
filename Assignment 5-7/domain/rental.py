from datetime import datetime
from datetime import timedelta


class Rental:

    def __init__(self, id=0, bookId=0, clientId=0, rentedDate="", dueDate="", returnedDate=""):
        self._id = id
        self._bookId = bookId
        self._clientId = clientId
        self._rentedDate = rentedDate
        self._dueDate = dueDate
        self._returnedDate = returnedDate

    def setId(self, value):
        self._id = value

    def getId(self):
        return self._id

    def getBookId(self):
        return self._bookId

    def setBookId(self, value):
        self._bookId = value

    def getClientId(self):
        return self._clientId

    def setClientId(self, value):
        self._clientId = value

    def getDueDate(self):
        return self._dueDate

    def setDueDate(self, value):
        self._dueDate = value

    def getRentedDate(self):
        return self._rentedDate

    def setRentedDate(self, value):
        self._rentedDate = value

    def setReturnedDate(self, value):
        self._returnedDate = value

    def getReturnedDate(self):
        return self._returnedDate

    def __str__(self):
        return "ID: " + str(self._id) + " | Book ID: " + str(self._bookId) + " | Client ID: " + str(
            self._clientId) + " | Rented Date: " + str(self._rentedDate) + " | Due Date: " + str(
            self._dueDate) + " | Returned Date " + str(self._returnedDate)

    def update(self, object):
        self.setBookId(object.getBookId())
        self.setClientId(object.getClientId())
        self.setReturnedDate(object.getReturnedDate())
        self.setRentedDate(object.getRentedDate())
        self.setDueDate(object.getDueDate())

    def __eq__(self, other):
        if self._bookId == other.getBookId() and self._clientId == other.getClientId() \
                and self._rentedDate == other.getRentedDate() and self._returnedDate == other.getReturnedDate() \
                and self._dueDate == other.getDueDate() and self._id == other.getId():
            return True
        return False

    @staticmethod
    def fromLine(line):
        params = line.split(";")
        return Rental(int(params[0]), int(params[1]), int(params[2]), params[3], params[4], params[5])

    @staticmethod
    def toLine(rental):
        return str(rental.getId()) + ';' + str(rental.getBookId()) + ';' + str(rental.getClientId()) + ";" + \
               str(rental.getRentedDate()) + ';' + str(rental.getDueDate()) + ';' + str(rental.getReturnedDate()) + '\n'

import unittest
import datetime
from controller.book_controller import BookController
from controller.client_controller import ClientController
from controller.rental_controller import RentalController, BookRental, ClientActivity, LateRental, AuthorRental
from controller.undo_controller import UndoController
from domain.book import Book
from domain.client import Client
from domain.rental import Rental
from exceptions import InvalidIdException, RepositoryException, InvalidNumberOfParametersException
from my_data_structure.my_data_structure import MyList
from repository.repository import Repository


class ControllerTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        undoController = UndoController()

        self.rentalList = Repository()
        self.bookList = Repository()
        self.clientList = Repository()

        self.rentalList.add(Rental(0, 0, 1, datetime.datetime.strptime("2017-10-10", '%Y-%m-%d'),
                                   datetime.datetime.strptime("2017-10-20", '%Y-%m-%d'), ""))
        self.rentalList.add(Rental(1, 1, 1, datetime.datetime.strptime("2017-10-10", '%Y-%m-%d'),
                                   datetime.datetime.strptime("2017-10-20", '%Y-%m-%d'), ""))



        self.bookList.add(Book(0,"book0", "desc0", "author0"))
        self.bookList.add(Book(1,"book1", "desc1", "author1"))
        self.bookList.add(Book(2,"book2", "desc2", "author2"))



        self.clientList.add(Client(0,"name0"))
        self.clientList.add(Client(1,"name1"))
        self.clientList.add(Client(2,"name2"))

        self.rentalController = RentalController(self.rentalList, self.bookList, self.clientList, undoController)
        self.bookController = BookController(self.bookList, undoController, self.rentalController)
        self.clientController = ClientController(self.clientList, undoController, self.rentalController)



    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testAddBook(self):

        self.bookController.addBook(3,"book3", "desc3","author3")
        self.assertEqual(self.bookList.getAll(), [Book(0,"book0", "desc0", "author0"), Book(1,"book1", "desc1", "author1"), Book(2,"book2", "desc2", "author2"),Book(3,"book3", "desc3", "author3")])

    def testAddClient(self):

        self.clientController.addClient(3, "name3")
        self.assertEqual(self.clientList.getAll(), [Client(0,"name0"), Client(1,"name1"), Client(2,"name2"), Client(3,"name3")])

    def testAddRental(self):

        rentalDate = datetime.datetime.now().date()
        self.rentalController.addRental(2, 2, 1)
        self.assertEqual(self.rentalList.getAll(), [
            Rental(0,0, 1, datetime.datetime.strptime("2017-10-10", '%Y-%m-%d'), datetime.datetime.strptime("2017-10-20", '%Y-%m-%d'), ""),
            Rental(1,1, 1, datetime.datetime.strptime("2017-10-10", '%Y-%m-%d'), datetime.datetime.strptime("2017-10-20", '%Y-%m-%d'), ""),
            Rental(2, 2, 1, rentalDate, rentalDate + datetime.timedelta(days=10), "")])
        try:
            self.rentalController.addRental(Rental(100, 1, datetime.datetime.strptime("2017-10-10", '%Y-%m-%d'),
                                                   datetime.datetime.strptime("2017-10-20", '%Y-%m-%d')))
            self.rentalController.addRental(Rental(2, 200, datetime.datetime.strptime("2017-10-10", '%Y-%m-%d'),
                                                   datetime.datetime.strptime("2017-10-20", '%Y-%m-%d')))
        except Exception:
            pass

    def testRemoveBook(self):

        self.bookController.removeBook(0)
        self.assertEqual(self.bookList.getAll(), [Book(1, "book1", "desc1", "author1"), Book(2, "book2", "desc2", "author2")])
        self.bookController.removeBook(2)
        self.bookController.removeBook(1)
        self.assertEqual(self.bookList.getAll(), [])
        with self.assertRaises(Exception):
            self.bookController.removeBook(10)

    def testRemoveClient(self):

        self.clientController.removeClient(1)
        self.assertEqual(self.clientList.getAll(), [Client(0, "name0"), Client(2, "name2")])
        with self.assertRaises(Exception):
            self.clientController.removeClient(100)

    def testRemoveRentalByClientId(self):

        self.rentalController.removeRentalByClientId(1)
        self.assertEqual(self.rentalList.getAll(), [])

    def testRemoveRentalByBookId(self):

        self.rentalController.removeRentalByBookId(0)
        self.assertEqual(self.rentalList.getAll(), [Rental(1, 1, 1, datetime.datetime.strptime("2017-10-10",'%Y-%m-%d'), datetime.datetime.strptime("2017-10-20" ,'%Y-%m-%d'), "")])

    def testUpdateBook(self):
        with self.assertRaises(InvalidIdException):
            self.bookController.updateBook(20, "book2", "author3", "desc4")

        self.bookController.updateBook(1, "Book1", "Author1", "Description1")
        self.assertEqual(self.bookList.get(1), Book(1,"Book1","Author1", "Description1"))

    def testUpdateClients(self):
        with self.assertRaises(InvalidIdException):
            self.clientController.updateClient(20, "Name1")
        self.clientController.updateClient(1, "Name1")
        self.assertEqual(self.clientList.get(1), Client(1, "Name1"))

    def testReturnBook(self):

        with self.assertRaises(Exception):
            self.rentalController.returnBook(100)
        self.rentalController.returnBook(0)
        self.assertEqual(self.rentalList.get(0), Rental(0, 0, 1, datetime.datetime.strptime("2017-10-10", '%Y-%m-%d'), datetime.datetime.strptime("2017-10-20", '%Y-%m-%d'), datetime.datetime.now().date()))

    def testGetBooks(self):

        self.assertEqual(self.bookController.getBooks() , [Book(0, "book0", "desc0", "author0"),
                                                           Book(1, "book1", "desc1", "author1"),
                                                           Book(2, "book2", "desc2", "author2")])

    def testGetClients(self):

        self.assertEqual(self.clientController.getClients(), [Client(0, "name0"), Client(1, "name1"), Client(2, "name2")])

    def testRentalVaidation(self):

        self.assertEqual(self.rentalController.rentalValidation(2, 1), True)

        with self.assertRaises(InvalidIdException):
            self.rentalController.rentalValidation(0,7)
            self.rentalController.rentalValidation(13, 0)

    def testMostRentedBooks(self):

        newList = self.rentalController.mostRentedBooks()
        self.assertEqual(newList, [BookRental(0, "book0", 1), BookRental(1, "book1", 1), BookRental(2, "book2", 0)])

    def testMostActiveClient(self):

        newList = self.rentalController.mostActiveClients()
        self.assertEqual(newList, [ClientActivity("name1", 20)])

    def testMostRentedAuthor(self):

        newList = self.rentalController.mostRentedAuthors()
        self.assertEqual(newList, [AuthorRental(0,"author0",1), AuthorRental(1, "author1", 1), AuthorRental(2, "author2", 0)])

    def testSearchBooks(self):

        searchList = self.bookController.searchBooks("book")
        self.assertEqual(searchList, [Book(0, "book0", "desc0", "author0"),
                                                           Book(1, "book1", "desc1", "author1"),
                                                           Book(2, "book2", "desc2", "author2")])
        self.bookList.add(Book(3, "book27", "desc3", "author4"))
        searchList1 = self.bookController.searchBooks("2")
        self.assertEqual(searchList1, [Book(2, "book2", "desc2", "author2"), Book(3, "book27", "desc3", "author4")])

    def testSearchClients(self):
        searchList = self.clientController.searchClients("cl")
        self.assertEqual(searchList, [])
        searchList1 = self.clientController.searchClients("na")
        self.assertEqual(searchList1, [Client(0, "name0"), Client(1, "name1"), Client(2, "name2")])

    # def testUndo(self):
    #     self.bookController.removeBook(1)
    #     self.bookController._undoController.undo()
    #     self.assertEqual(self.bookList.getAll(), [Book(0, "book0", "desc0", "author0"),
    #                                      Book(2, "book2", "desc2", "author2"),
    #                                      Book(1, "book1", "desc1", "author1")])
    #
    #     self.clientController.removeClient(1)
    #     self.clientController._undoController.undo()
    #     self.assertEqual(self.clientList.getAll(), [Client(0, "name0"), Client(2, "name2"), Client(1, "name1")])
    #
    #     self.rentalController.returnBook(0)
    #     self.rentalController._undoController.undo()
    #     self.assertEqual(self.rentalList.get(0), Rental(0, 0, 1, datetime.datetime.strptime("2017-10-10",'%Y-%m-%d'), datetime.datetime.strptime("2017-10-20" ,'%Y-%m-%d'), ""))
    #

    # def cascadeUndoTest(self):
    #     pass


class RepositoryTest(unittest.TestCase):

    def testRepository(self):
        bookRepo = Repository()
        testList = [Book(0, "book0", "desc0", "author0"),
                    Book(1, "book1", "desc1", "author1")]
        for i in range(0, len(testList)):
            bookRepo.add(testList[i])
            self.assertEqual(bookRepo.get(i), testList[i])
        bookRepo.update(1, Book(0, "Book1", "Author1", "Description1"))
        self.assertEqual(bookRepo.get(1), Book(1,"Book1", "Author1", "Description1"))

class MyDataStructure(unittest.TestCase):

    def testList(self):
        list = MyList()
        self.assertEqual(len(list), 0)
        for i in range(0, 10):
            list.append(i)
        self.assertEqual(len(list), 10)
        for i in list:
            self.assertEqual(list[i], i)

        list.pop(7)
        self.assertEqual(len(list), 9)
        del list[4]
        self.assertEqual(len(list), 8)
        list.remove(1)
        self.assertEqual(len(list), 7)
        list[5] = "Andreea"
        self.assertEqual(list[5], "Andreea")
        list[2] = list[5]
        self.assertEqual(list[2], "Andreea")

    def testSort(self):
        list = MyList()
        for i in range(4, -1, -1):
            list.append(i)
        list.sort()
        sortList = MyList()
        for i in range(0, 5):
            sortList.append(i)
        self.assertEqual(list, sortList)

class SortingAlgorithmTest(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        self.rentalList = MyList()
        self.bookList = MyList()
        self.clientList = MyList()
        self.rentalList.append(Rental(0, 0, 1, datetime.datetime.strptime("2017-10-10", '%Y-%m-%d'),
                                   datetime.datetime.strptime("2017-10-20", '%Y-%m-%d'), ""))
        self.rentalList.append(Rental(1, 1, 1, datetime.datetime.strptime("2017-10-10", '%Y-%m-%d'),
                                   datetime.datetime.strptime("2017-10-20", '%Y-%m-%d'), ""))

        self.bookList.append(Book(0, "book0", "desc0", "author1"))
        self.bookList.append(Book(1, "book1", "desc1", "author0"))
        self.bookList.append(Book(2, "book2", "desc2", "author2"))

        self.clientList.append(Client(0, "name1"))
        self.clientList.append(Client(1, "name0"))
        self.clientList.append(Client(2, "name2"))

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testSortObject(self):
        self.clientList.sort(key=lambda x:x.getName())
        self.assertEqual(self.clientList[0],Client(1, "name0"))
        self.assertEqual(self.clientList[1],Client(0, "name1"))
        self.assertEqual(self.clientList[2],Client(2, "name2"))

        self.bookList.sort(key=lambda x: x.getTitle(), reverse=True)
        self.assertEqual(self.bookList[0], Book(2, "book2", "desc2", "author2"))
        self.assertEqual(self.bookList[1], Book(1, "book1", "desc1", "author0"))
        self.assertEqual(self.bookList[2], Book(0, "book0", "desc0", "author1"))

    def testFilter(self):
        res = self.clientList.filter(key=lambda x: x.getName(), value="name1")
        self.assertEqual(res[0], Client(0, "name1"))
        res1 = self.bookList.filter(key=lambda x: x.getId(), value=0)
        self.assertEqual(res1[0], Book(0, "book0", "desc0", "author1"))
        res2 = self.clientList.filter()
        self.assertEqual(res2, self.clientList)
        self.clientList.append(Client(3, "name0"))
        res3 = self.clientList.filter(key=lambda x:x.getName(), value="name0")
        self.assertEqual(res3[0], Client(1, "name0"))
        self.assertEqual(res3[1], Client(3, "name0"))

if __name__ == '__main__':
    unittest.main()

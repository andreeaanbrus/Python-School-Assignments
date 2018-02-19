from controller.book_controller import BookController
from controller.client_controller import ClientController
from controller.rental_controller import RentalController
from controller.undo_controller import UndoController
from domain.book import Book
from domain.client import Client
from domain.rental import Rental
from repository.binary_file_repository import BinaryFileRepository
from repository.repository import Repository
from repository.text_file_repository import TextFileRepository
from settings.properties import Settings
from test import testInitBooks, testInitRentals
from test import testInitClients
from ui.ui import UI


settings = Settings()

if settings.getRepository() == "in-memory":
    bookRepo = Repository()
    clientRepo = Repository()
    rentalRepo = Repository()
    testInitBooks(bookRepo)
    testInitClients(clientRepo)
    testInitRentals(rentalRepo)

elif settings.getRepository() == "text-file":
    bookRepo = TextFileRepository("books.csv", Book.fromLine, Book.toLine)
    clientRepo = TextFileRepository("clients.csv", Client.fromLine, Client.toLine)
    rentalRepo = TextFileRepository("rentals.csv", Rental.fromLine, Rental.toLine)

elif settings.getRepository() == "binary":
    bookRepo = BinaryFileRepository("books.pickle")
    clientRepo = BinaryFileRepository("clients.pickle")
    rentalRepo = BinaryFileRepository("rentals.pickle")

undoController = UndoController()
rentalController = RentalController(rentalRepo, bookRepo, clientRepo, undoController)
bookController = BookController(bookRepo, undoController, rentalController)
clientController = ClientController(clientRepo, undoController, rentalController)

ui = UI(bookController, clientController, rentalController, undoController)
ui.start()

import datetime

from domain.book import Book
from domain.client import Client
from domain.rental import Rental

def testInitBooks(repo):
    repo.add(Book(0,"Harry Potter and the Philosopher's Stone ", "first book of HP series", "J.K. Rowling"))
    repo.add(Book(1,"Harry Potter and the Chamber of Secrets ", "second book of HP series", "J.K. Rowling"))
    repo.add(Book(2,"Harry Potter and the Prisoner of Azkaban ", "third book of HP series", "J.K. Rowling"))
    repo.add(Book(3,"Harry Potter and the Goblet of Fire ", "4th book of HP series", "J.K. Rowling"))
    repo.add(Book(4,"Harry Potter and the Order of Phoenix ", "5th book of HP series", "J.K. Rowling"))
    repo.add(Book(5,"Harry Potter and the Half-Blood Prince ", "6th book of HP series", "J.K. Rowling"))
    repo.add(Book(6,"Harry Potter and the Deathly Hallows ", "7th book of HP series", "J.K. Rowling"))
    repo.add(Book(7,"The Great Gatsby", "-", "F. Scott Fitzgerald"))
    repo.add(Book(8,"The Alchimist", "", "Paulo Coelho"))
    repo.add(Book(9,"A Flew Over the Cuckoo's Nest", "mental health", "Ken Kesey"))

def testInitClients(repo):
    for i in range(0, 10):
        repo.add(Client(i, "client"+str(i)))

def testInitRentals(repo):

    for i in range(0, 10):
        repo.add(Rental(i, i, i, datetime.datetime.now().date(), datetime.datetime.now().date() + datetime.timedelta(days=10), datetime.datetime(2017, 12, 1).date()))
    for i in range(10, 20):
        repo.add(Rental(i, i-10, i - 10, datetime.datetime(2017,4,27).date(), datetime.datetime(2017,4,27).date() + datetime.timedelta(days=10), ""))

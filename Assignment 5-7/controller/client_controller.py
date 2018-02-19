import copy
import re

from controller.undo_controller import FunctionCall, Operation, CascadeOperation
from domain.client import Client
from exceptions import InvalidIdException


class ClientController():
    def __init__(self, repository, undoController, rentalController):
        self._clientRepo = repository
        self._undoController = undoController
        self._rentalController = rentalController

    def addClient(self, id, name, recordForUndo = True):
        """
        Adds a new client in the list
        :param client: class Client
        :return: the client added
        """
        if self.checkId(id) == False:
            raise InvalidIdException
        client = Client(id,name)

        if recordForUndo == True:
            undo = FunctionCall(self.removeClient, id, False)
            redo = FunctionCall(self.addClient, id, name, False)
            operation = Operation(redo, undo)
            self._undoController.recordOperation(operation)
        self._clientRepo.add(client)
        return client

    def getClients(self):
        """
        Gets all clients from the list
        :return: all clients
        """
        return self._clientRepo.getAll()

    def removeClient(self, id, recordForUndo = True):
        """
        Removes a client from a list
        :param id: the id of the client
        :return: the client
        """

        client = self.findClientById(id)
        index = self.findIndexInRepo(id)
        oldClient = copy.deepcopy(client)
        cascadeOp = CascadeOperation()
        if recordForUndo == True:
            list = self._rentalController.removeRentalByClientId(id)
            for i in range(len(list)-1, -1, -1):
                undo_casc = FunctionCall(self._rentalController.addRental, list[i].getId(), list[i].getBookId(),
                                         list[i].getClientId(), list[i].getRentedDate(), list[i].getDueDate(),
                                         list[i].getReturnedDate(), False)
                redo_casc = FunctionCall(self._rentalController.removeRental, list[i].getId(), False)
                op = Operation(redo_casc, undo_casc)
                cascadeOp.add(op)

            undo = FunctionCall(self.addClient, client.getId(), client.getName(), False)
            redo = FunctionCall(self.removeClient, client.getId(), False)
            operation = Operation(redo, undo)
            cascadeOp.add(operation)
            self._undoController.recordOperation(cascadeOp)


        self._clientRepo.remove(client)
        return oldClient


    def updateClient(self, id, name, recordForUndo = True):
        """
        Updates a client with a certain id with a new one
        :param id: the id of the old (and new) client - int
        :param client: the new name
        :return: -
        """

        if self.checkId(id) == True:
            raise InvalidIdException
        client = self.findClientById(id)
        index = self.findIndexInRepo(id)
        if recordForUndo == True:
            undo = FunctionCall(self.updateClient, id, client.getName(), False)
            redo = FunctionCall(self.updateClient, id, name, False)
            operation = Operation(redo, undo)
            self._undoController.recordOperation(operation)

        newClient = Client(id, name)
        self._clientRepo.update(index, newClient)
        return newClient

    def searchClients(self, params):
        """
        find all clients by a given substring
        :param params: the givent substring
        :return: the list of matches
        """
        list = []
        token = str(params[0])
        for i in self._clientRepo.getAll():
            if re.search(token, i.getName(), re.IGNORECASE) or re.search(token, str(i.getId()), re.IGNORECASE):
                list.append(i)
        return list

    def findIndexInRepo(self, clientId):
        """

        :param clientId: the clientId
        :return: the index in the repository of the client
        """
        index = 0
        for i in self._clientRepo.getAll():
            if i.getId() != clientId:
                index += 1
            else:
                return index
        raise InvalidIdException

    def findClientByIndex(self, index):
        """
        gets the element from the list
        """
        return self._clientRepo.getAll()[index]

    def findClientById(self, id):
        """
        finds the client with a certain id
        """
        for i in self._clientRepo.getAll():
            if i.getId() == id:
                return i


    def checkId(self, id):
        """
        Checks if there exists another object with that id
        :param id: the given id, int
        :return: True, False
        """
        for i in self._clientRepo.getAll():
            if i.getId() == id:
                return False
        return True


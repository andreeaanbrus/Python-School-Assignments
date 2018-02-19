from exceptions import InvalidIdException, InvalidCommandException, InvalidNumberOfParametersException


class UI:
    def __init__(self, bookController, clientController, rentalController, undoController):
        self._bookController = bookController
        self._clientController = clientController
        self._rentalController = rentalController
        self._undoController = undoController

    @staticmethod
    def uiHelp():
        print("#add_book <id> <title>, <description>, <author>")
        print("#add_client <id>, <name>")
        print("#list_books")
        print("#list_clients")
        print("#remove_book <index>")
        print("#remove_list <index>")
        print("#update_book <index> <title> <description> <author>")
        print("#update_client <index> <name>")
        print("#rent_book <id>, <bookId>, <clientId>")
        print("#return_book <bookId>")
        print("#search_in_books <string>")
        print("#search_in_client <string>")
        print("#most_rented_books")
        print("#most_rented_authors")
        print("#most_active_clients")
        print("#late_rentals")
        print("#undo")
        print("#redo")

    @staticmethod

    def readCommand():
        """
        Read and parse user command
        :return:    (command, params) tuple where
                    command - string = user command
                    object - string = the object to operate with
                    params - string = parameters
        """
        cmd = input("command: ")
        if cmd.find(" ") == -1:
            '''
            No parameters
            '''
            command = cmd
            params = ""
        else:
            '''
            We have parameters
            '''
            command = cmd[0:cmd.find(" ")]
            params = cmd[cmd.find(" ") + 1:]
            params = params[0:].split(',')
            for i in range(0, len(params)):
                params[i] = params[i].strip()
        return (command, params)

    def start(self):
        while True:
            try:
                cmd = UI.readCommand()
                command = cmd[0]
                params = cmd[1]

                if command == 'add_book':
                    [id, title, description, author] = UI.uiGetBook(params)
                    self._bookController.addBook(id, title, description, author)
                    print("The book was added!")

                elif command == 'add_client':
                    [id,name] = UI.uiAddClient(params)
                    self._clientController.addClient(id, name)
                    print("The client was added!")

                elif command == 'list_books':
                    for n in self._bookController.getBooks():
                        print(n)

                elif command == 'list_clients':
                    for n in self._clientController.getClients():
                        print(n)

                elif command == 'remove_book':
                    id = UI.uiGetIndex(params)
                    self._bookController.removeBook(id)
                    print("The book was removed!")

                elif command == 'remove_client':
                    id = UI.uiGetIndex(params)
                    self._clientController.removeClient(id)
                    print("The client was removed!")

                elif command == 'update_book':
                    id = UI.uiGetIndex(params)
                    [title, description, author] = UI.uiGetUpdateBook(params)
                    self._bookController.updateBook(id, title, description, author)
                    print("The book was updated!")

                elif command == 'update_client':
                    id = UI.uiGetIndex(params)
                    client = UI.uiGetUpdateClient(params)
                    self._clientController.updateClient(id, client)
                    print("The client was updated!")

                elif command == 'rent_book':
                    if len(params) != 3:
                        raise InvalidNumberOfParametersException("The parameters should be <bookId>, <clientId>")
                    self._rentalController.addRental(int(params[0]), int(params[1]), int(params[2]))
                    print("The rental was added")

                elif command == 'list_rentals':
                    for n in self._rentalController.getRentals():
                        print(n)

                elif command == 'return_book':
                    bookId = UI.uiGetIndex(params)
                    self._rentalController.returnBook(bookId)
                    print("The book was returned")

                elif command == 'search_in_books':
                    list = self._bookController.searchBooks(params)
                    if len(list):
                        for i in list:
                            print(i)
                    else:
                        print("No match was found!")

                elif command == 'search_in_clients':
                    list = self._clientController.searchClients(params)
                    if len(list):
                        for i in list:
                            print(i)
                    else:
                        print("No match was found!")

                elif command == 'most_rented_books':
                    list = self._rentalController.mostRentedBooks()
                    for i in list:
                        print(i)

                elif command == 'most_rented_authors':
                    list = self._rentalController.mostRentedAuthors()
                    for i in list:
                        print(i)

                elif command == 'late_rentals':
                    list = self._rentalController.lateRentals()
                    for i in list:
                        print(i)

                elif command == 'most_active_clients':
                    list = self._rentalController.mostActiveClients()
                    for i in list:
                        print(i)

                elif command == 'undo':
                    if self._undoController.undo() == False:
                        raise Exception("No more undos to do")
                    print("Undo was done!")

                elif command == 'redo':
                    if self._undoController.redo() == False:
                        raise Exception("No more redos to do")
                    print("Redo was done!")
                elif command =='remove_rental':
                    self._rentalController.removeRental(int(params[0]))
                elif command == 'help':
                    UI.uiHelp()

                elif command == 'exit':
                    break
                else:
                        raise InvalidCommandException()
            except Exception as exc:
                print("Error encountered - " + str(exc))

    @staticmethod
    def uiGetBook(params):
        """
        Return the book formed with the params
        :param params: the given params
        :return: the object (BOOK)
        """
        if len(params) != 4:
            raise InvalidNumberOfParametersException("The parameters should be <id>, <title>, <description>, <author>")
        id = int(params[0])
        title = params[1]
        description = params[2]
        author = params[3]
        return [id, title, description, author]

    @staticmethod
    def uiAddClient(params):
        """
        :param params: the given parameters (name)
        :return: the client object formed with the params
        """
        if len(params) != 2:
            raise InvalidNumberOfParametersException("The parameter should be <id>, <name>")
        if params[1] == "":
            raise InvalidNumberOfParametersException("The parameter should be <id>, <name>")
        id = int(params[0])
        name = params[1]
        return [id, name]

    @staticmethod
    def uiGetIndex(params):
        """
        :param params: the given parameters (id)
        :return:id = the id of the book
        """
        if not params[0].isdecimal():
            raise InvalidIdException("The id should be a number")
        id = int(params[0])
        return id

    @staticmethod
    def uiGetUpdateBook(params):
        """
        :param params: the given parameters for the new book
        :return: book = the new book
        """
        if len(params) != 4:
            raise InvalidNumberOfParametersException("The parameters should be <index>, <title>, "
                                                     "<description> and <author>")
        title = params[1]
        description = params[2]
        author = params[3]

        return title, description, author

    @staticmethod
    def uiGetUpdateClient(params):
        """
        :param params: the given parameters for updating a client
        :return: client-object; the new client
        """
        if len(params) != 2:
            raise InvalidNumberOfParametersException("The parameters should be <id>, <name>")
        name = params[1]
        return name


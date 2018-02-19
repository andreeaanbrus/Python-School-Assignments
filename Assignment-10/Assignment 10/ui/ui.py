
class UI:
    def __init__(self, controller):
        self._controller = controller

    def start(self):

        while not self._controller.checkIfWon():
            try:
                self._controller.printBoard()
                column = int(input("Your move! Give the column number: "))
                if not 0 <= column <= 7:
                    raise Exception("The column number should be between 1 and 7")
                column -= 1
                self._controller.movePlayer(column)
                if self._controller.checkIfWon():
                    print("You won!")
                    break
                self._controller.moveComputer()
                if self._controller.checkIfWon():
                    print("You lost! :(")
                    break
                if self._controller.checkIfDraw():
                    print("It is draw!")
                    break
            except Exception as e:
                 print(e)

        self._controller.printBoard()
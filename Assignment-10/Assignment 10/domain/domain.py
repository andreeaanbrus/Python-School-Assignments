

class Square:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

    def getY(self):
        return self._y

    def setY(self, value):
        self._y = value


class Board:
    def __init__(self):
        self._board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.lastAdded = None

        # self.move(Square(5, 0), "player")
        # self.move(Square(5, 2), "player")
        # self.move(Square(5, 4), "player")
        # self.move(Square(5, 6), "player")
        # self.move(Square(4, 1), "player")
        # self.move(Square(4, 3), "player")
        # self.move(Square(4, 5), "player")
        # self.move(Square(3, 0), "player")
        # self.move(Square(3, 2), "player")
        # self.move(Square(3, 4), "player")
        # self.move(Square(3, 6), "player")
        # self.move(Square(2, 0), "player")
        # self.move(Square(2, 2), "player")
        #
        # self.move(Square(5, 1), "computer")
        # self.move(Square(5, 3), "computer")
        # self.move(Square(5, 5), "computer")
        # self.move(Square(4, 0), "computer")
        # self.move(Square(4, 2), "computer")
        # self.move(Square(4, 4), "computer")
        # self.move(Square(4, 6), "computer")
        # self.move(Square(3, 1), "computer")
        # self.move(Square(3, 3), "computer")
        # self.move(Square(3, 5), "computer")
        # self.move(Square(2, 1), "computer")
        # self.move(Square(2, 3), "computer")
        # self.move(Square(2, 5), "computer")

    def move(self, square, sign):
        """
        makes a move
        """
        if square.getX() < 0 or square.getX() > 8 or square.getY() < 0 or square.getY() > 7:
            raise Exception("Not in the board")

        if self._board[square.getX()][square.getY()] != 0:
            raise Exception("The place is already taken")

        if sign == 'player':
            self._board[square.getX()][square.getY()] = 1
        if sign == 'computer':
            self._board[square.getX()][square.getY()] = -1

        self.lastAdded = square.getY()

    def freeSquares(self):
        """
        decide which are the free squares
        """
        cnt = 0
        for i in range(0, 6):
            for j in range(0, 7):
                if self._board[i][j] == 0:
                    cnt += 1
        return cnt

    def checkFreeSquaresOnColumn(self, column):
        """
        Checks if there are free squares on a certain column
        :return: True-if there are
                False-otherwise
        """
        for i in range(5, -1, -1):
            if self._board[i][column] == 0:
                return True
        return False

    def isWon(self):
        """
        :return: decides if a game is won or not
        """
        """
        Check horizontally
        """
        for j in range(0, 4):
            for i in range(0, 6):
                if self._board[i][j] == 1 or self._board[i][j] == -1:
                    if self._board[i][j] == self._board[i][j+1] == self._board[i][j+2] == self._board[i][j+3]:
                        return True
        """
        Check vertically
        """
        for i in range(0, 3):
            for j in range(0, 7):
                if self._board[i][j] == 1 or self._board[i][j] == -1:
                    if self._board[i][j] == self._board[i+1][j] == self._board[i+2][j] == self._board[i+3][j]:
                        return True

        """
        Check first diagonal
        """
        for i in range(0, 3):
            for j in range(0, 4):
                if self._board[i][j] == 1 or self._board[i][j] == -1:
                    if self._board[i][j] == self._board[i+1][j+1] == self._board[i+2][j+2] == self._board[i+3][j+3]:
                        return True

        """
        Check second diagonal
        """
        for i in range(0, 3):
            for j in range(3, 7):
                if self._board[i][j] == 1 or self._board[i][j] == -1:
                    if self._board[i][j] == self._board[i+1][j-1] == self._board[i+2][j-2] == self._board[i+3][j-3]:
                        return True

        return False

    def isDraw(self):
        """
        :return: decides if is draw or not
                True, False
        """
        for i in range(0, 6):
            for j in range(0, 7):
                if self._board[i][j] == 0:
                    return False
        return True

    def findNextFreeSquareOnColumn(self, column):
        """

        :param column: the number of the current column
        :return: i - the next free square (there exists for sure a new free square)
        """
        for i in range(5, -1, -1):
            if self._board[i][column] == 0:
                res = i
                return res

    def __str__(self):
        string = ""
        for i in range(0, 6):
            for j in range(0, 7):
                if self._board[i][j] == 1:
                    string += '*' + ' | '
                if self._board[i][j] == -1:
                    string += '$' + ' | '
                if self._board[i][j] == 0:
                    string += ' ' + ' | '
            string += '\n' + 27 * '-' + '\n'
        return string

    def getlastAdded(self):
        return self.lastAdded

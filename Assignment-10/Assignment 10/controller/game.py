import copy

from domain.domain import Square


class Game:
    def __init__(self, board):
        self._board = board
        self.recursions = 0

    def moveComputer(self):
        """
        verific patratele libere
        pun mutare noua
        random la inceput
        """
        j = None
        best_score = -10000
        for column in range(7):
            if not self._board.checkFreeSquaresOnColumn(column):
                continue
            next_board = copy.deepcopy(self._board)
            i = next_board.findNextFreeSquareOnColumn(column)
            next_board.move(Square(i, column), "computer")
            score = self.__minmax(next_board, 1)
            #print("%s : %s" % (column, score), end="    ")
            if score > best_score:
                best_score = score
                j = column

        #print("placing %s, recursions = %s" % (j + 1, self.recursions))
        self.recursions = 0
        i = self._board.findNextFreeSquareOnColumn(j)
        self._board.move(Square(i, j), "computer")

    def __minmax(self, board, depth):
        """
        :return: column to play, score if played
        """
        self.recursions += 1
        # print(board, depth, self.recursions)
        # input("enter")
        # print(board)
        if depth > 4:
            return -100

        score = None

        if board.isDraw():
            return 0

        elif board.isWon():
            if depth % 2 == 0:
                # when comp turn, table is won, so comp lost
                return -200
            if depth % 2 == 1:
                # when human turn if table is won, comp won
                return 100

        else:
            for column in range(0, 7):
                if not board.checkFreeSquaresOnColumn(column):
                    continue
                next_board = copy.deepcopy(board)
                i = next_board.findNextFreeSquareOnColumn(column)
                if depth % 2 == 0:
                    # if depth is even, it means that the computer is moving
                    next_board.move(Square(i, column), "computer")
                if depth % 2 == 1:
                    # if depth is odd, then the human is moving
                    next_board.move(Square(i, column), "player")

                # after everything is set, recursive call to find the next score
                next_score = self.__minmax(next_board, depth+1)

                if depth % 2 == 0:
                    # if the computer is at turn, maximize the possible result
                    if score is None:
                        score = next_score
                    elif score < next_score:
                        score = next_score
                if depth % 2 == 1:
                    # if the human is at turn, minimize the possible result
                    if score is None:
                        score = next_score
                    elif score > next_score:
                        score = next_score

        return score - 10

    def movePlayer(self, column):
        """
        verific liber
        pun mutare noua
        """
        if not self._board.checkFreeSquaresOnColumn(column):
            raise Exception("You can not complete anymore on this column")
        i = self._board.findNextFreeSquareOnColumn(column)
        self._board.move(Square(i, column), "player")

    def checkIfWon(self):
        """
        Check if the game is won after every move
        :return: True - if it is won
                False-otherwise
        """
        if self._board.isWon():
            return True
        return False

    def checkIfDraw(self):
        """
        Check if it is draw after every move
        :return: True -if draw
                False - otherwise
        """
        if self._board.isDraw():
            return True
        return False

    def printBoard(self):
        print(self._board)

import unittest

from controller.game import Game
from domain.domain import Board, Square


class MyTestCase(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self._board = Board()
        self._controller = Game(self._board)

    def testcheckFreeSquaresOnColumn(self):
        self._board.move(Square(0, 1), "computer")
        self._board.move(Square(1, 1), "computer")
        self._board.move(Square(2, 1), "computer")
        self._board.move(Square(3, 1), "computer")
        self._board.move(Square(4, 1), "computer")
        self.assertEqual(self._board.checkFreeSquaresOnColumn(1), True)
        self._board.move(Square(5, 1), "computer")
        self.assertEqual(self._board.checkFreeSquaresOnColumn(1), False)

    def testCheckIsWon(self):
        self._board.move(Square(0, 1), "computer")
        self._board.move(Square(1, 1), "computer")
        self._board.move(Square(2, 1), "computer")
        self.assertEqual(self._board.isWon(), False)
        self._board.move(Square(3, 1), "computer")
        self.assertEqual(self._board.isWon(), True)



    def tearDown(self):
        unittest.TestCase.tearDown(self)

if __name__ == '__main__':
    unittest.main()

from controller.game import Game
from domain.domain import Board
from ui.ui import UI

board = Board()
controller = Game(board)
ui = UI(controller)
ui.start()

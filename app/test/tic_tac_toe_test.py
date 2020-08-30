import unittest
from app.main.games.tic_tac_toe import TicTacToe

class TicTacToeTests(unittest.TestCase):

    def test_should_win_player_one(self):
        # Arrange
        game = TicTacToe(3)

        game.add_player('A')
        game.add_player('B')

        # Act 
        game.move(1,1, 'A')
        game.move(0,1, 'B')
        game.move(0,0, 'A')
        game.move(2,2, 'B')
        result = game.move(2,2, 'A')

        # Assert

        self.assertEqual(result, 'A')
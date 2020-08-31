from collections import defaultdict
class UserState():
    def __init__(self):
        self.rows = defaultdict(int)
        self.cols = defaultdict(int)
        self.left_diagonal = 0
        self.right_diagonal = 0

'''
348. Design Tic-Tac-Toe - https://leetcode.com/problems/design-tic-tac-toe/
'''
class TicTacToe():
    def __init__(self, board_size):
        self.board_size = board_size

        self.state = {}

    def add_player(self, player):
        self.state[player] = UserState()

    def move(self, row, col, player):
        self.state[player].rows[row] += 1
        self.state[player].cols[col] += 1

        if row == col:
            self.state[player].left_diagonal += 1

        if row == (self.board_size - col - 1):
            self.state[player].right_diagonal += 1

        return self.get_winner(player, row, col)

    def get_winner(self, player, row, col):
        row_count = self.state[player].rows[row]
        col_count = self.state[player].cols[col]
        left_diagonal = self.state[player].left_diagonal
        right_diagonal = self.state[player].right_diagonal

        if row_count == self.board_size:
            return player

        if col_count == self.board_size:
            return player

        if left_diagonal == self.board_size:
            return player

        if right_diagonal == self.board_size:
            return player

        return 0
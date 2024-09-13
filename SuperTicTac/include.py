import random as rd

class SuperTicTacToe:
    def __init__(self):
        self.sub_board_checks = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.current_sub_board = [rd.randint(0, 2), rd.randint(0, 2)]
        self.winner = None
        self.super_board = [[[[' ' for _ in range(3)] 
                              for _ in range(3)]
                             for _ in range(3)] 
                            for _ in range(3)]

    def draw_console(self):
        print("In sub-board: ", self.current_sub_board)
        # print(self.super_board)
        print("      0       1       2    ")
        for i in range(3):
            print("  ╔       ╦       ╦       ╗")
            for j in range(3):
                if j==1: print(i, end=' ')
                else : print(" ", end=' ')
                print("║", end=' ')
                for k in range(3):
                    for l in range(3):
                        print(self.super_board[i][k][j][l], end=' ')
                    print("║", end=' ')
                print()
            print("  ╚       ╩       ╩       ╝")
    

    def turn_subboard(self, row, col):
        self.current_sub_board = [row, col]

    def check_winner(self):
        for i in range(3):
            if self.sub_board_checks[i][0] == self.sub_board_checks[i][1] == self.sub_board_checks[i][2] != ' ':
                return True
            if self.sub_board_checks[0][i] == self.sub_board_checks[1][i] == self.sub_board_checks[2][i] != ' ':
                return True
        if self.sub_board_checks[0][0] == self.sub_board_checks[1][1] == self.sub_board_checks[2][2] != ' ':
            return True
        if self.sub_board_checks[0][2] == self.sub_board_checks[1][1] == self.super_board[2][0] != ' ':
            return True
        return False
    
    def assign(self, row, col):
        self.super_board[self.current_sub_board[0]] \
                        [self.current_sub_board[1]][row][col] = self.current_player

    def check_winner_sub_board(self, row, col):
        for i in range(3):
            if self.super_board[row][col][i][0] == self.super_board[row][col][i][1] == self.super_board[row][col][i][2] != ' ':
                return True
            if self.super_board[row][col][0][i] == self.super_board[row][col][1][i] == self.super_board[row][col][2][i] != ' ':
                return True
        if self.super_board[row][col][0][0] == self.super_board[row][col][1][1] == self.super_board[row][col][2][2] != ' ':
            return True
        if self.super_board[row][col][0][2] == self.super_board[row][col][1][1] == self.super_board[row][col][2][0] != ' ':
            return True
        return False
    
    def draw_win_sub_board(self, row, col):
        print("Win sub-board: ", row, col)
        # draw X or O on the sub-board
        self.super_board[row][col] = [['*' for _ in range(3)] for _ in range(3)]
        if self.sub_board_checks[row][col] == 'O':
            self.super_board[row][col][1][1] = ' '
        else:
            self.super_board[row][col][0][1] = ' '
            self.super_board[row][col][1][0] = ' '
            self.super_board[row][col][1][2] = ' '
            self.super_board[row][col][2][1] = ' '

    def play(self, row, col):
        if self.winner:
            print(f'{self.winner} wins the game!')
            return

        if self.super_board[self.current_sub_board[0]] \
                           [self.current_sub_board[1]][row][col] != ' ':
            print('Invalid move')
            return

        self.assign(row, col)

        if self.check_winner_sub_board(self.current_sub_board[0], self.current_sub_board[1]):
            self.sub_board_checks[self.current_sub_board[0]] \
                                 [self.current_sub_board[1]] = self.current_player
            self.draw_win_sub_board(self.current_sub_board[0], self.current_sub_board[1])

            if self.check_winner():
                self.winner = self.current_player
                

        if not self.check_winner_sub_board(row, col):
            self.turn_subboard(row, col)
        else:
            print('Sub-board already won by', self.sub_board_checks[row][col])

            
        self.current_player = 'O' if self.current_player == 'X' else 'X'
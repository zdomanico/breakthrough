


class Breakthrough():
    def __init__(self):
        super(Breakthrough,self).__init__()
        self.n = 8

        self.board = []
        for i in range(0, self.n):
            self.board.append([])
            for j in range(0, self.n):
                if i <= 1:
                    self.board[i].append('x')
                elif i >= 6:
                    self.board[i].append('o')
                else:
                    self.board[i].append('.')

    def print_board(self):
        print(self.board)
        for i in range(0, self.n):
            for j in range(0, self.n):
                print(self.board[i][j], end=' ')
            print()


c = Breakthrough()
c.print_board()

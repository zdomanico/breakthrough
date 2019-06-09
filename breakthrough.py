


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
        # print(self.board)
        for i in range(0, self.n):
            for j in range(0, self.n):
                print(self.board[i][j], end=' ')
            print()

    def check_win(self):
        if 'o' in self.board[0]:
            return 'o'
        elif 'x' in self.board[self.n - 1]:
            return 'x'
        return '.'

    def valid(self, turn, start_x, start_y, end_x, end_y):
        start_piece = self.board[start_x][start_y]
        end_piece = self.board[end_x][end_y]
        if start_piece == end_piece or turn != start_piece:
            return False
        if start_piece  == '.':
            return False
        if start_piece == 'x':
            if end_x != start_x + 1:
                return False
            if end_y < start_y - 1 or end_y > start_y + 1:
                return False
            if end_y == start_y and end_piece == 'o':
                return False
        if start_piece == 'o':
            if end_x != start_x - 1:
                return False
            if end_y < start_y - 1 or end_y > start_y + 1:
                return False
            if end_y == start_y and end_piece == 'x':
                return False
        return True
    def move(self, turn, start_x, start_y, end_x, end_y):
        if self.valid(turn, start_x, start_y, end_x, end_y):
            self.board[end_x][end_y] = self.board[start_x][start_y]
            self.board[start_x][start_y] = '.'
            self.print_board()
            return True
        return False

    def get_move(self):
        a = int(input())
        b = int(input())
        c = int(input())
        d = int(input())
        return (a, b, c, d)

    def play_game(self):
        self.print_board()
        turn = 'x'
        while self.check_win() == '.':
            print("Enter move player " + turn + ":")
            m = self.get_move()
            if (self.move(turn, m[0], m[1], m[2], m[3])):
                turn = 'x' if turn == 'o' else 'o'
        print("There is a winner: " + self.check_win() + " won!")

c = Breakthrough()
c.print_board()

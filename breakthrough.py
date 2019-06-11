


class Breakthrough():
    def __init__(self):
        super(Breakthrough,self).__init__()
        self.n = 8
        self.turn = 'x'

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
    def change_turn(self):
        self.turn = 'x' if self.turn == 'o' else 'o'
    def get_turn(self):
        return self.turn
    def print_board(self):
        # print(self.board)
        for i in range(0, self.n):
            for j in range(0, self.n):
                print(self.board[i][j], end=' ')
            print()
    def reset(self):
        self.turn = 'x'
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

    def check_win(self):
        if 'o' in self.board[0]:
            return 'o'
        elif 'x' in self.board[self.n - 1]:
            return 'x'
        return '.'

    def valid(self, turn, start_x, start_y, end_x, end_y):
        start_piece = self.board[start_x][start_y]
        end_piece = self.board[end_x][end_y]
        if start_x < 0 or start_x >= self.n:
            return False
        if start_y < 0 or start_y >= self.n:
            return False
        if end_x < 0 or end_x >= self.n:
            return False
        if end_y < 0 or end_y >= self.n:
            return False
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
                self.print_board()
                turn = 'x' if turn == 'o' else 'o'
        print("There is a winner: " + self.check_win() + " won!")

from breakthrough import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Example(QWidget):
    keyPressed = pyqtSignal(QEvent)
    def __init__(self):
        super(Example, self).__init__()
        self.margin = 10
        self.cmd = ""
        self.n = 8
        self.xy = 800 + 2 * self.margin
        self.initUI()
        self.highlight_list = []
        self.game = Breakthrough()
        self.x = -1
        self.y = -1
        self.game_on = True
    def initUI(self):

        self.setGeometry(self.xy, self.xy, self.xy, self.xy)
        self.setWindowTitle('Breakthrough')
        self.show()
        self.keyPressed.connect(self.on_key)
        size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        size_policy.setHeightForWidth(True)
        self.setSizePolicy(size_policy)

    def heightForWidth(self, width):
        return width
    def resizeEvent(self, e):
        new_size = QSize(10, 10)
        new_size.scale(e.size(), Qt.KeepAspectRatio)
        self.resize(new_size)

    def get_cell_size(self):
        return (self.height() - 2 * self.margin) // self.n

    def mousePressEvent(self, QMouseEvent):
        if not self.game_on:
            return
        x = QMouseEvent.x()
        y = QMouseEvent.y()
        wh = self.get_cell_size()
        b = (x - self.margin) // wh
        a = (y - self.margin) // wh
        if a < 0 or a >= self.n or b >= self.n or b < 0:
            return
        if (self.x == -1 or self.y == -1) and \
                self.game.board[a][b] == self.game.get_turn():
            self.highlight_list.append((a, b))
            self.x = a
            self.y = b
            for i in range(min(a - 1, 0), min(a + 2, self.game.n)):
                for j in range(min(b - 1, 0), min(self.game.n, b + 2)):
                    print((i, j))
                    if self.game.valid(self.game.get_turn(), a, b, i, j):
                        self.highlight_list.append((i, j))
        elif (self.x == a and self.y == b):
            self.highlight_list = []
            self.x = -1
            self.y = -1
        elif (a, b) in self.highlight_list:
            self.game.move(self.game.get_turn(), self.x, self.y, a, b)
            self.game.change_turn()
            self.highlight_list= []
            self.x = -1
            self.y = -1
        print(a, b)
        if (self.game.check_win() != '.'):
            winner = 'black' if self.game.check_win() == 'x' else 'white'
            print("There is a winner: " + winner + " won!")
            print("Press r to reset the board and play again.")
            self.game_on = False
        self.update()

    def keyPressEvent(self, event):
        super(Example, self).keyPressEvent(event)
        self.keyPressed.emit(event)

    def highlight_cell(self, qp):
        qp.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        wh = self.get_cell_size()
        for y, x in self.highlight_list:
            qp.drawRect(self.margin + wh * x, self.margin + wh * y, wh, wh)
    def un_highlight_cell(self, x, y):
        qp = QPainter()
        qp.begin(self)
        wh = self.get_cell_size()
        qp.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        qp.drawRect(self.margin + wh * x, self.margin + wh * y, wh, wh)
        qp.end()

    def on_key(self, event):
        if event.key() == Qt.Key_Q:
            print("Killing")
            self.deleteLater()
        elif event.key() == Qt.Key_R:
            self.game_on = True
            self.game.reset()
            self.update()

    def proceed(self):
        print("Call Enter Key")

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)

        qp.setBrush(QBrush(Qt.lightGray, Qt.SolidPattern))
        qp.drawRect(0, 0, int(self.width()), int(self.height()))
        self.drawRectangles(qp)
        self.highlight_cell(qp)
        for i in range(self.game.n):
            for j in range(self.game.n):
                if self.game.board[i][j] == 'x':
                    self.draw_circle(qp, j, i, 'b')
                elif self.game.board[i][j] == 'o':
                    self.draw_circle(qp, j, i, 'w')
        qp.end()

    def drawRectangles(self, qp):
        counter = 0
        wh = self.get_cell_size()
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        for i in range(self.n):
            for j in range(self.n):
                qp.drawRect(self.margin + wh * (counter // self.n), self.margin + wh * (counter % self.n), wh, wh)
                counter += 1
    def draw_circle(self, qp, x, y, c):

        qp.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        if c == 'b':
            qp.setBrush(QBrush(Qt.black, Qt.SolidPattern))
        elif c == 'w':
            qp.setBrush(QBrush(Qt.white, Qt.SolidPattern))

        wh = self.get_cell_size()
        r = int(.4 * wh)
        real_x = self.margin + wh * x + wh // 2
        real_y = self.margin + wh * y + wh // 2
        qp.drawEllipse(QPoint(real_x, real_y), r, r)


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

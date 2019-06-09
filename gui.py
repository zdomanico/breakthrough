
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
        x = QMouseEvent.x()
        y = QMouseEvent.y()
        wh = self.get_cell_size()
        b = (x - self.margin) // wh
        a = (y - self.margin) // wh
        print(a, b)
        if (a,b) in self.highlight_list:
            self.highlight_list.remove((a,b))
        else:
            self.highlight_list.append((a, b))
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
        elif event.key() == Qt.Key_Left:
            self.game.change_color(-1)
            self.update()
        elif event.key() == Qt.Key_Right:
            self.game.change_color(1)
            self.update()
        elif event.key() == Qt.Key_Enter:
            print("Enter!")
            self.game.confirm_selection()
            self.update()
        elif event.key() == Qt.Key_U:
            self.highlight_cell(0, 0)
            self.update()
        elif event.key() == Qt.Key_I:
            self.un_highlight_cell(0, 0)
            self.update()
        elif event.key() < 1000:
            self.cmd += chr(event.key())
            if len(self.cmd) == 4:
                print(self.cmd + " Calling move handler!")
                self.game.get_move_wrapper(self.cmd)
                self.update()
                self.cmd = ""
                self.game.check_win()

    def proceed(self):
        print("Call Enter Key")

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)

        qp.setBrush(QBrush(Qt.lightGray, Qt.SolidPattern))
        qp.drawRect(0, 0, int(self.width()), int(self.height()))
        self.drawRectangles(qp)
        self.draw_circle(qp, 0, 0, 'w')
        self.highlight_cell(qp)
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

import sys
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import QPointF, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint
from Ui import Ui_MainWindow
class Circle(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.size = 500
        self.setWindowTitle('Circle')
        self.flag = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.drawCircle(qp)
            qp.end()
        self.flag = False

    def paint(self):
        self.flag = True
        self.update()

    def drawCircle(self, qp):
        h = randint(10, self.size)
        x, y = randint(10, self.size - 10), randint(10, self.size - 10)
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        qp.setPen(QColor(r, g, b))
        qp.drawEllipse(QPointF(x, y), h / 2, h / 2)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec())
import sys
import random

from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow


class Circles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.circle)
        self.data = []

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(255, 255, 0))
        for x, y, w in self.data:
            qp.drawEllipse(x, y, w, w)
        qp.end()

    def circle(self):
        w = random.randint(3, 350)
        x = random.randint(1, 600 - w)
        y = random.randint(1, 600 - w)
        self.data.append((x, y, w))
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())

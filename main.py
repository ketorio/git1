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
        self.x = 0
        self.y = 0
        self.w = 0

    def circle(self):
        self.w = random.randint(3, 550)
        self.x = random.randint(1, 600 - self.w)
        self.y = random.randint(1, 600 - self.w)
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(self.x, self.y, self.w, self.w)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())


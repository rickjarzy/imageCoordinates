import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QLabel)
from PyQt5.QtGui import QPixmap


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap(r"drone_data/rgb.JPG")

        image_label = QLabel(self)
        image_label.setPixmap(pixmap)
        image_label.mousePressEvent = self.get_pixel

        hbox.addWidget(image_label)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Dronen RGB')
        self.show()

    def get_pixel(self, event):
        x = event.pos().x()
        y = event.pos().y()
        print("\nselected coords\nx: %d - y: %d"%(x,y))
        return x, y





if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

print("Programm ENDE")

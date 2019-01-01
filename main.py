import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton)
from PyQt5.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget<br>HTML geht')

        button = QPushButton('Button', self)
        button.setToolTip('This is a <b>Pushbutton</b><br><i>HTML geht</i>')
        button.resize(button.sizeHint())
        button.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("ToolTips")
        self.show()


if __name__ == "__main__":
    print(sys.argv)
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


print("Programm ENDE")

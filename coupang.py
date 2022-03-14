from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class MyWindow(QWidget):
    def __init__(self):
        print('hi')


    def setupUI(self):
        print('setup')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
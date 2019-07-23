
from PyQt5.QtWidgets import QMainWindow
from .BoardGUI import BoardGUI


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(700, 200, 800, 500)
        self.setStyleSheet(open("src/gui/styleSheet/style.qss", "r").read())
        board = BoardGUI()
        self.setCentralWidget(board)


from PyQt5.QtWidgets import QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(800, 200, 500, 500)
        button = QPushButton("test temp")
        self.setCentralWidget(button)

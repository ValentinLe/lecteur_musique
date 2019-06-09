
from model.Board import Board
import sys
from PyQt5.QtWidgets import QApplication
from gui.MainWindow import MainWindow


def mainGUI():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    path = "C:/Users/Val/Desktop/Dossier/testLecteur"
    mainGUI()

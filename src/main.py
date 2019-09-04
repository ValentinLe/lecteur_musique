
import sys
import ctypes
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QColor
from model.Board import Board
from gui.MainWindow import MainWindow


def mainGUI():
    app = QApplication(sys.argv)

    try:
        # ajout de l'id de l'application
        myappid = 'ValentinLe.lecteur_musique'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except AttributeError:
        pass

    # ajout de l'icone de l'application
    app.setWindowIcon(QIcon(QPixmap("assets/logo.png")))

    # couleurs pour la scrollBar
    palette = QPalette()
    palette.setColor(QPalette.Base, QColor("#454545"))
    palette.setColor(QPalette.Light, QColor("#454545"))
    app.setPalette(palette)

    # affichage de la fenetre principale
    board = Board()
    window = MainWindow(board)
    window.setWindowTitle("Musique")
    window.showMaximized()
    # window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    mainGUI()

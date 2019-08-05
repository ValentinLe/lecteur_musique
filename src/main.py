
import sys
import ctypes
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon, QPixmap
from gui.MainWindow import MainWindow


def mainGUI():
    app = QApplication(sys.argv)

    # ajout de l'id de l'application
    myappid = 'ValentinLe.lecteur_musique'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app.setWindowIcon(QIcon(QPixmap("assets/logo.ico")))

    window = MainWindow()
    window.showMaximized()
    # window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    path = "C:/Users/Val/Desktop/Dossier/testLecteur"
    mainGUI()

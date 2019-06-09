
from PyQt5.QtWidgets import QWidget, QGridLayout
from .QueueSong import QueueSong
from model.Board import Board


class BoardGUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        path = "C:/Users/Val/Desktop/Dossier/testLecteur"
        b = Board()
        b.addSongOfDirectory(path)
        b.moveSongToPrimary(1)
        b.moveSongToPrimary(0)
        primaryQueue = QueueSong(b.getPrimaryQueue())
        secondaryQueue = QueueSong(b.getSecondaryQueue())

        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(primaryQueue, 0, 0)
        layout.addWidget(secondaryQueue, 0, 1)

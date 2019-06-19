
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from model.Board import Board
from .QueueSong import QueueSong
from .PlayerSound import PlayerSound


class BoardGUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        path = "C:/Users/Val/Desktop/Dossier/musiques"
        self.b = Board()
        self.b.addSongOfDirectory(path)
        self.b.secondaryQueue.shuffle(10)
        self.primaryQueue = QueueSong(
            self.b, self.b.getPrimaryQueue(), self.b.getSecondaryQueue())
        self.secondaryQueue = QueueSong(
            self.b, self.b.getSecondaryQueue(), self.b.getPrimaryQueue())

        self.b.addListener(self.primaryQueue)
        self.b.addListener(self.secondaryQueue)

        self.b.nextSong()
        self.player = PlayerSound(self.b)
        self.b.addListener(self.player)

        layout = QVBoxLayout()
        self.setLayout(layout)
        queueSongs = QHBoxLayout()
        queueSongs.addWidget(self.primaryQueue)
        queueSongs.addWidget(self.secondaryQueue)
        layout.addLayout(queueSongs)
        layout.addWidget(self.player)

    def moveToPrimary(self):
        indexSelected = self.secondaryQueue.getIndexSelected()
        if indexSelected >= 0:
            self.b.moveSongToPrimary(indexSelected)

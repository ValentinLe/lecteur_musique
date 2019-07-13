
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.Qt import Qt
from PyQt5.QtCore import QEvent
from model.Board import Board
from .QueueSong import QueueSong
from .PlayerSound import PlayerSound
from .SearchSong import SearchSong


class BoardGUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        path = "C:/Users/Val/Desktop/Dossier/musiques"
        self.b = Board()
        self.b.addSongOfDirectory(path)
        self.b.secondaryQueue.shuffle(10)

        self.searchSong = SearchSong(self.b)

        labPrimary = QLabel("Liste d'attente principale")
        labPrimary.setAlignment(Qt.AlignCenter)
        self.primaryQueue = QueueSong(
            self.b, self.b.getPrimaryQueue(), self.b.getSecondaryQueue())
        labSecondary = QLabel("Liste d'attente secondaire")
        labSecondary.setAlignment(Qt.AlignCenter)
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
        queueSongs.addWidget(self.searchSong)

        primaryQueueLayout = QVBoxLayout()
        primaryQueueLayout.addWidget(labPrimary)
        primaryQueueLayout.addWidget(self.primaryQueue)

        secondaryQueueLayout = QVBoxLayout()
        secondaryQueueLayout.addWidget(labSecondary)
        secondaryQueueLayout.addWidget(self.secondaryQueue)

        queueSongs.addLayout(primaryQueueLayout)
        queueSongs.addLayout(secondaryQueueLayout)

        layout.addLayout(queueSongs)
        layout.addWidget(self.player)

    def keyReleaseEvent(self, event):
        if event.key() == 16777344:
            self.player.play()
        elif event.key() == 16777346:
            self.player.precedentSong()
        elif event.key() == 16777347:
            self.player.nextSong()

    def moveToPrimary(self):
        indexSelected = self.secondaryQueue.getIndexSelected()
        if indexSelected >= 0:
            self.b.moveSongOfIndexToPrimary(indexSelected)

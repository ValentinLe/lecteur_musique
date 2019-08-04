
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.Qt import Qt
from model.Board import Board
from .QueueSong import QueueSong
from .PlayerSound import PlayerSound
from .SearchSong import SearchSong


class BoardGUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        path = "C:/Users/Val/Desktop/Dossier/musiques"
        self.changeSong = True
        self.b = Board()
        self.b.addSongOfDirectory(path)
        self.b.secondaryQueue.shuffle(10)

        self.searchSong = SearchSong(self.b)

        labPrimary = QLabel("Liste d'attente prioritaire")
        labPrimary.setProperty("class", "title")
        labPrimary.setAlignment(Qt.AlignCenter)
        self.primaryQueue = QueueSong(
            self.b, self.b.getPrimaryQueue(), self.b.getSecondaryQueue())
        labSecondary = QLabel("Liste d'attente")
        labSecondary.setProperty("class", "title")
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

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            self.searchSong.clearSearch()
        if event.key() == Qt.Key_MediaPlay or event.key() == Qt.Key_MediaPause:
            self.player.play()
        else:
            if self.changeSong:
                self.changeSong = False
                if event.key() == Qt.Key_MediaPrevious:
                    self.player.precedentSong()
                elif event.key() == Qt.Key_MediaNext:
                    self.player.nextSong()
                else:
                    self.changeSong = True
            else:
                self.changeSong = True

    def moveToPrimary(self):
        indexSelected = self.secondaryQueue.getIndexSelected()
        if indexSelected >= 0:
            self.b.moveSongOfIndexToPrimary(indexSelected)

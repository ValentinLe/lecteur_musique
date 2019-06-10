
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton
from .QueueSong import QueueSong
from .PlayerSound import PlayerSound
from model.Board import Board


class BoardGUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        path = "C:/Users/Val/Desktop/Dossier/testLecteur"
        self.b = Board()
        self.b.addSongOfDirectory(path)
        self.b.secondaryQueue.shuffle(10)
        self.b.moveSongToPrimary(1)
        self.b.moveSongToPrimary(0)
        self.primaryQueue = QueueSong(self.b.getPrimaryQueue())
        self.secondaryQueue = QueueSong(self.b.getSecondaryQueue())

        bMove = QPushButton("<<<")
        bMove.clicked.connect(self.moveToPrimary)

        player = PlayerSound()

        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.primaryQueue, 0, 0)
        layout.addWidget(bMove, 0, 1)
        layout.addWidget(self.secondaryQueue, 0, 2)
        layout.addWidget(player, 1, 1)

    def moveToPrimary(self):
        indexSelected = self.secondaryQueue.getIndexSelected()
        if indexSelected >= 0:
            self.b.moveSongToPrimary(indexSelected)
            print(self.b)


from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer


class PlayerSound(QWidget):
    def __init__(self, board):
        QWidget.__init__(self)

        self.board = board
        self.player = QMediaPlayer()
        self.songName = QLabel(self.board.getCurrentSong().getName())
        self.setSongInPlayer()
        self.player.mediaStatusChanged.connect(self.mediaFinished)

        self.bPlay = QPushButton("Play")
        self.bPlay.clicked.connect(self.play)
        bNext = QPushButton("Next")
        bNext.clicked.connect(self.nextSong)

        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.songName, 0, 0)
        layout.addWidget(self.bPlay, 0, 1)
        layout.addWidget(bNext, 0, 2)

    def mediaFinished(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.nextSong()

    def play(self):
        state = self.player.state()
        if state == QMediaPlayer.StoppedState or state == QMediaPlayer.PausedState:
            self.player.play()
            self.bPlay.setText("Pause")
        else:
            self.player.pause()
            self.bPlay.setText("Play")

    def nextSong(self):
        self.board.nextSong()
        self.player.stop()
        self.setSongInPlayer()
        self.play()

    def setSongInPlayer(self):
        song = self.board.getCurrentSong()
        url = QUrl.fromLocalFile(song.getFullFilename())
        self.player.setMedia(QMediaContent(url))

    def update(self):
        song = self.board.getCurrentSong()
        self.songName.setText(song.getName())

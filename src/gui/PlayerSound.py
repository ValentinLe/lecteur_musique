
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer


class PlayerSound(QWidget):
    def __init__(self, board):
        QWidget.__init__(self)

        self.board = board
        self.board.addListener(self)

        self.player = QMediaPlayer()

        self.songName = QLabel(self.board.getCurrentSong().getName())

        bPlay = QPushButton("Play")
        bPlay.clicked.connect(self.play)
        bNext = QPushButton("Next")
        bNext.clicked.connect(self.nextSong)

        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.songName, 0, 0)
        layout.addWidget(bPlay, 0, 1)
        layout.addWidget(bNext, 0, 2)

    def play(self):
        state = self.player.state()
        if state == QMediaPlayer.StoppedState or state == QMediaPlayer.PausedState:
            self.player.play()
        else:
            self.player.pause()

    def nextSong(self):
        song = self.board.nextSong()
        self.player.stop()
        url = QUrl.fromLocalFile(song.getFullFilename())
        self.player.setMedia(QMediaContent(url))
        self.play()

    def update(self):
        song = self.board.getCurrentSong()
        self.songName.setText(song.getName())

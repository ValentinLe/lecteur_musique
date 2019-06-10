
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QSlider
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer


class PlayerSound(QWidget):
    def __init__(self, board):
        QWidget.__init__(self)

        self.board = board
        self.player = QMediaPlayer()
        self.songName = QLabel(self.board.getCurrentSong().getName())
        self.setSongInPlayer()
        self.player.mediaStatusChanged.connect(self.mediaFinished)
        self.player.durationChanged.connect(self.changeSliderDuration)
        self.player.positionChanged.connect(self.changeSliderPosition)

        self.bPlay = QPushButton("Play")
        self.bPlay.clicked.connect(self.play)
        bNext = QPushButton("Next")
        bNext.clicked.connect(self.nextSong)

        self.sliderSong = QSlider(Qt.Horizontal)
        self.sliderSong.valueChanged.connect(self.changePosition)

        self.labelVolume = QLabel("100")
        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setValue(100)
        self.volumeSlider.valueChanged.connect(self.changeVolume)

        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.songName, 0, 0)
        layout.addWidget(self.bPlay, 0, 1)
        layout.addWidget(bNext, 0, 2)
        layout.addWidget(self.volumeSlider, 0, 3)
        layout.addWidget(self.labelVolume, 1, 3)
        layout.addWidget(self.sliderSong, 1, 0)

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

    def changePosition(self, position):
        self.player.pause()
        self.player.setPosition(position)
        self.player.play()

    def changeSliderPosition(self, position):
        self.sliderSong.setValue(position)

    def changeSliderDuration(self, duration):
        self.sliderSong.setMaximum(duration)

    def changeVolume(self):
        valueVolume = self.volumeSlider.value()
        self.player.setVolume(valueVolume)
        self.labelVolume.setText(str(valueVolume))

    def update(self):
        song = self.board.getCurrentSong()
        self.songName.setText(song.getName())

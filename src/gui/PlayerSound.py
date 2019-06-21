
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSlider, QLayout
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer


class PlayerSound(QWidget):
    def __init__(self, board):
        QWidget.__init__(self)

        self.board = board
        currentSong = self.board.getCurrentSong()
        self.player = QMediaPlayer()
        self.songName = QLabel(currentSong.getName())
        self.songName.setMinimumWidth(200)
        self.songName.setMaximumWidth(200)
        self.songAuthor = QLabel(currentSong.getAuthor())
        self.player.mediaStatusChanged.connect(self.mediaFinished)
        self.player.positionChanged.connect(self.changeSliderPosition)

        self.bPlay = QPushButton("Play")
        self.bPlay.clicked.connect(self.play)
        bNext = QPushButton("Next")
        bNext.clicked.connect(self.nextSong)

        self.sliderSong = QSlider(Qt.Horizontal)
        self.sliderSong.sliderMoved.connect(self.changePosition)
        self.labCurrentDuration = QLabel("0:00")
        self.labMaxDuration = QLabel("0:00")

        self.labelVolume = QLabel("100")
        self.labelVolume.setAlignment(Qt.AlignCenter)
        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setMinimumWidth(200)
        self.volumeSlider.setMaximumWidth(200)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setValue(100)
        self.volumeSlider.valueChanged.connect(self.changeVolume)

        self.setSongInPlayer()

        # position elements

        leftInfoSong = QVBoxLayout()
        leftInfoSong.addWidget(self.songName)
        leftInfoSong.addWidget(self.songAuthor)

        centerPlayer = QVBoxLayout()
        buttonsPlayer = QHBoxLayout()
        buttonsPlayer.addWidget(self.bPlay)
        buttonsPlayer.addWidget(bNext)
        centerPlayer.addLayout(buttonsPlayer)
        sliderWithTime = QHBoxLayout()
        sliderWithTime.addWidget(self.labCurrentDuration)
        sliderWithTime.addWidget(self.sliderSong)
        sliderWithTime.addWidget(self.labMaxDuration)
        centerPlayer.addLayout(sliderWithTime)

        rightVolume = QVBoxLayout()
        rightVolume.addWidget(self.labelVolume)
        rightVolume.addWidget(self.volumeSlider)

        # positionnement global
        layout = QHBoxLayout()
        self.setLayout(layout)
        layout.addLayout(leftInfoSong)
        layout.addStretch()
        layout.addLayout(centerPlayer)
        layout.addStretch()
        layout.addLayout(rightVolume)

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
        self.sliderSong.setMaximum(song.getDuration())
        self.labMaxDuration.setText(self.getStrDuration(song.getDuration()))

    def changePosition(self, position):
        self.player.setPosition(position)

    def changeSliderPosition(self, position):
        self.sliderSong.setValue(position)
        self.update()

    def changeVolume(self):
        valueVolume = self.volumeSlider.value()
        self.player.setVolume(valueVolume)
        self.labelVolume.setText(str(valueVolume))

    def getStrDuration(self, millis):
        secondes = millis // 1000
        minutes = secondes // 60
        secondes = secondes % 60
        res = str(minutes) + ":"
        if secondes < 10:
            res += "0"
        res += str(secondes)
        return res

    def update(self):
        song = self.board.getCurrentSong()
        self.songName.setText(song.getName())
        self.songAuthor.setText(song.getAuthor())
        self.labCurrentDuration.setText(
            self.getStrDuration(self.player.position()))

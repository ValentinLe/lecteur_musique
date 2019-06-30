
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSlider
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from util.StringDuration import getStrDuration


class PlayerSound(QWidget):
    def __init__(self, board):
        QWidget.__init__(self)

        self.board = board
        self.isPlaying = False
        self.isChangingPosition = None

        currentSong = self.board.getCurrentSong()
        self.player = QMediaPlayer()
        self.songName = QLabel(currentSong.getName())
        self.songName.setMinimumWidth(200)
        self.songName.setMaximumWidth(200)
        self.songAuthor = QLabel(currentSong.getAuthor())
        self.player.mediaStatusChanged.connect(self.mediaFinished)
        self.player.positionChanged.connect(self.changeSliderPosition)

        bPrecedent = QPushButton("Precedent")
        bPrecedent.clicked.connect(self.precedentSong)
        self.bPlay = QPushButton("Play")
        self.bPlay.clicked.connect(self.play)
        bNext = QPushButton("Next")
        bNext.clicked.connect(self.nextSong)

        self.sliderSong = QSlider(Qt.Horizontal)
        self.sliderSong.sliderPressed.connect(self._sliderPauseSong)
        self.sliderSong.sliderReleased.connect(self._sliderPlaySong)
        self.labCurrentDuration = QLabel("0:00")
        self.volumeSlider = QSlider(Qt.Horizontal)
        self.labMaxDuration = QLabel("0:00")

        self.bMute = QPushButton("o")
        self.bMute.setMaximumWidth(80)
        self.bMute.clicked.connect(self.mute)
        self.labelVolume = QLabel("100")
        self.labelVolume.setAlignment(Qt.AlignCenter)
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
        buttonsPlayer.addWidget(bPrecedent)
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
        sliderAndMuteLayout = QHBoxLayout()
        sliderAndMuteLayout.addWidget(self.bMute)
        sliderAndMuteLayout.addWidget(self.volumeSlider)
        rightVolume.addLayout(sliderAndMuteLayout)

        # positionnement global
        layout = QHBoxLayout()
        self.setLayout(layout)
        layout.addLayout(leftInfoSong)
        layout.addStretch()
        layout.addLayout(centerPlayer)
        layout.addStretch()
        layout.addLayout(rightVolume)

    def _sliderPauseSong(self):
        if self.isPlaying:
            self.player.pause()

    def _sliderPlaySong(self):
        positionSlider = self.sliderSong.value()
        self.player.setPosition(positionSlider)
        if self.isPlaying:
            self.player.play()

    def mediaFinished(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.nextSong()

    def play(self):
        state = self.player.state()
        if state == QMediaPlayer.StoppedState or state == QMediaPlayer.PausedState:
            self.player.play()
            self.bPlay.setText("Pause")
            self.isPlaying = True
        else:
            self.player.pause()
            self.bPlay.setText("Play")
            self.isPlaying = False

    def mute(self):
        isMuted = self.player.isMuted()
        self.player.setMuted(not isMuted)
        if isMuted:
            self.bMute.setText("o")
        else:
            self.bMute.setText("x")

    def nextSong(self):
        self.board.nextSong()
        self.player.stop()
        self.setSongInPlayer()
        if self.isPlaying:
            self.play()

    def precedentSong(self):
        state = self.player.state()
        stateStop = QMediaPlayer.StoppedState
        statePause = QMediaPlayer.PausedState
        playerStoped = state == stateStop or state == statePause
        if not playerStoped:
            self.player.stop()
        self.board.precedentSong()
        self.setSongInPlayer()
        if not playerStoped:
            self.player.play()

    def setSongInPlayer(self):
        song = self.board.getCurrentSong()
        url = QUrl.fromLocalFile(song.getFullFilename())
        self.player.setMedia(QMediaContent(url))
        self.sliderSong.setMaximum(song.getDuration())
        self.labMaxDuration.setText(getStrDuration(song.getDuration()))

    def changeSliderPosition(self, position):
        self.sliderSong.setValue(position)
        self.update()

    def getPositionPlayer(self, positionSlider):
        maxDuration = self.player.duration()
        durationSong = self.board.getCurrentSong().getDuration()
        if durationSong != 0:
            return positionSlider * maxDuration // durationSong
        else:
            return 0

    def getPositionSlider(self, positionPlayer):
        maxDuration = self.player.duration()
        durationSong = self.board.getCurrentSong().getDuration()
        if maxDuration != 0:
            return positionPlayer * durationSong // maxDuration
        else:
            return 0

    def changeVolume(self):
        valueVolume = self.volumeSlider.value()
        self.player.setVolume(valueVolume)
        self.labelVolume.setText(str(valueVolume))

    def update(self):
        song = self.board.getCurrentSong()
        self.songName.setText(song.getName())
        self.songAuthor.setText(song.getAuthor())
        self.labCurrentDuration.setText(
            getStrDuration(self.player.position()))

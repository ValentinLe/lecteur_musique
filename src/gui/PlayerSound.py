
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSlider
from PyQt5.QtCore import QUrl, Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from util.StringDuration import getStrDuration
from gui.ConfigWindow import ConfigWindow


class PlayerSound(QWidget):
    '''
    represente le lecteur de musique, permettant de mettre pause/play, changer de musique, etc.

    :param board: le tableau de bord du lecteur
    :type board: model.Board
    '''

    def __init__(self, board, parent=None):
        QWidget.__init__(self, parent)

        # hauteur du lecteur
        heightWindow = 125
        self.setMinimumHeight(heightWindow)
        self.setMaximumHeight(heightWindow)

        # images des bouttons
        self.iconPlay = QIcon(QPixmap("assets/play.png"))
        self.iconPause = QIcon(QPixmap("assets/pause.png"))
        iconNext = QIcon(QPixmap("assets/next.png"))
        iconPrecedent = QIcon(QPixmap("assets/precedent.png"))
        iconShuffle = QIcon(QPixmap("assets/shuffle.png"))
        iconReplay = QIcon(QPixmap("assets/replay.png"))
        self.iconSoundOn = QIcon(QPixmap("assets/soundOn.png"))
        self.iconSoundOff = QIcon(QPixmap("assets/soundOff.png"))
        iconConfig = QIcon(QPixmap("assets/config.png"))
        # taille des bouttons
        iconSize = QSize(50, 50)

        self.board = board
        self.isPlaying = False
        self.isChangingPosition = None

        # lecteur Qt et musique en cours
        currentSong = self.board.getCurrentSong()
        self.player = QMediaPlayer()
        self.songName = QLabel(currentSong.getName())
        self.songName.setProperty("class", "songName")
        self.songName.setWordWrap(True)
        self.songName.setFixedWidth(310)
        self.songAuthor = QLabel(currentSong.getAuthor())
        self.songAuthor.setProperty("class", "author")
        self.player.mediaStatusChanged.connect(self.mediaFinished)
        self.player.positionChanged.connect(self.changeSliderPosition)

        # bouttons au dessus de la barre de progression de la lecture de la musique
        bShuffle = QPushButton()
        bShuffle.setToolTip("Melanger la liste d'attente")
        bShuffle.setFixedSize(iconSize)
        bShuffle.setIcon(iconShuffle)
        bShuffle.setIconSize(iconSize)
        bShuffle.clicked.connect(self.shuffle)
        bPrecedent = QPushButton()
        bPrecedent.setToolTip("Musique precedente")
        bPrecedent.setFixedSize(iconSize)
        bPrecedent.setIcon(iconPrecedent)
        bPrecedent.setIconSize(iconSize)
        bPrecedent.clicked.connect(self.precedentSong)
        self.bPlay = QPushButton()
        self.bPlay.setFixedSize(iconSize)
        self.bPlay.setIcon(self.iconPlay)
        self.bPlay.setIconSize(iconSize)
        self.bPlay.clicked.connect(self.play)
        bNext = QPushButton()
        bNext.setFixedSize(iconSize)
        bNext.setIcon(iconNext)
        bNext.setIconSize(iconSize)
        bNext.clicked.connect(self.nextSong)
        bReplay = QPushButton()
        bReplay.setToolTip("Rejouer")
        bReplay.setFixedSize(iconSize)
        bReplay.setIcon(iconReplay)
        bReplay.setIconSize(iconSize)
        bReplay.clicked.connect(self.replay)

        # barre de progression de la lecture de la musique en cours
        self.sliderSong = QSlider(Qt.Horizontal)
        self.sliderSong.setMinimumWidth(600)
        self.sliderSong.setMaximumWidth(600)
        self.labCurrentDuration = QLabel("0:00")
        self.labCurrentDuration.setProperty("class", "duration")
        self.volumeSlider = QSlider(Qt.Horizontal)
        self.labMaxDuration = QLabel("0:00")
        self.labMaxDuration.setProperty("class", "duration")

        # controles sur le son de la musique
        self.bMute = QPushButton()
        self.bMute.setIcon(self.iconSoundOn)
        self.bMute.setFixedSize(iconSize)
        self.bMute.setIconSize(iconSize)
        self.bMute.clicked.connect(self.mute)
        self.labelVolume = QLabel("100")
        self.labelVolume.setAlignment(Qt.AlignCenter)
        self.volumeSlider.setFixedWidth(250)
        self.volumeSlider.setValue(100)
        self.volumeSlider.valueChanged.connect(self.changeVolume)

        # boutton pour ouvrir la fenetre de parametres
        bParams = QPushButton()
        bParams.setToolTip("Parametres")
        bParams.setFixedSize(iconSize)
        bParams.setIcon(iconConfig)
        bParams.setIconSize(iconSize)
        bParams.clicked.connect(self.openParams)

        # position elements

        leftInfoSong = QVBoxLayout()
        leftInfoSong.addWidget(self.songName)
        leftInfoSong.addWidget(self.songAuthor)

        centerPlayer = QVBoxLayout()
        buttonsPlayer = QHBoxLayout()
        buttonsPlayer.addStretch()
        buttonsPlayer.addWidget(bShuffle)
        buttonsPlayer.addSpacing(8)
        buttonsPlayer.addWidget(bPrecedent)
        buttonsPlayer.addSpacing(8)
        buttonsPlayer.addWidget(self.bPlay)
        buttonsPlayer.addSpacing(8)
        buttonsPlayer.addWidget(bNext)
        buttonsPlayer.addSpacing(8)
        buttonsPlayer.addWidget(bReplay)
        buttonsPlayer.addStretch()
        centerPlayer.addLayout(buttonsPlayer)
        sliderWithTime = QHBoxLayout()
        sliderWithTime.addWidget(self.labCurrentDuration)
        sliderWithTime.addWidget(self.sliderSong)
        sliderWithTime.addWidget(self.labMaxDuration)
        centerPlayer.addLayout(sliderWithTime)

        rightVolumeParam = QVBoxLayout()
        sliderAndMuteLayout = QHBoxLayout()
        sliderAndMuteLayout.addWidget(self.bMute)
        sliderAndMuteLayout.addWidget(self.volumeSlider)
        rightVolumeParam.addLayout(sliderAndMuteLayout)
        otherButtonsZone = QHBoxLayout()
        otherButtonsZone.addStretch()
        otherButtonsZone.addWidget(bParams)
        otherButtonsZone.addStretch()
        rightVolumeParam.addLayout(otherButtonsZone)

        # positionnement global
        layout = QHBoxLayout()
        self.setLayout(layout)
        layout.addLayout(leftInfoSong)
        layout.addStretch()
        layout.addLayout(centerPlayer)
        layout.addStretch()
        layout.addLayout(rightVolumeParam)

    def mediaFinished(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.nextSong()

    def shuffle(self):
        self.board.shuffle(5)

    def replay(self):
        self.player.setPosition(0)
        self.sliderSong.setValue(0)
        self.update()

    def play(self):
        state = self.player.state()
        currentSong = self.board.getCurrentSong()
        if currentSong:
            if state == QMediaPlayer.PausedState or state == QMediaPlayer.StoppedState:
                if state == QMediaPlayer.StoppedState:
                    self.setSongInPlayer()
                self.player.play()
                self.bPlay.setIcon(self.iconPause)
                self.isPlaying = True
            else:
                self.player.pause()
                self.bPlay.setIcon(self.iconPlay)
                self.isPlaying = False

    def mute(self):
        isMuted = self.player.isMuted()
        self.player.setMuted(not isMuted)
        if isMuted:
            self.bMute.setIcon(self.iconSoundOn)
        else:
            self.bMute.setIcon(self.iconSoundOff)

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
        ''' set la musique courante dans le lecteur Qt '''
        song = self.board.getCurrentSong()
        url = QUrl.fromLocalFile(song.getFullFilename())
        self.player.setMedia(QMediaContent(url))
        # set du temps maximum pour la barre de progression
        self.sliderSong.setMaximum(song.getDuration())
        self.labMaxDuration.setText(getStrDuration(song.getDuration()))

    def changeSliderPosition(self, position):
        self.sliderSong.setValue(position)
        self.update()

    def changeVolume(self):
        valueVolume = self.volumeSlider.value()
        self.player.setVolume(valueVolume)

    def openParams(self):
        w = QMainWindow(self)
        w.setCentralWidget(ConfigWindow(self.board, w))
        w.setGeometry(650, 500, 600, 150)
        w.setStyleSheet(open("src/gui/styleSheet/styleParam.qss", "r").read())
        w.setWindowTitle("Parametres")
        w.show()

    def update(self):
        song = self.board.getCurrentSong()
        if song:
            self.songName.setText(song.getName())
            self.songAuthor.setText(song.getAuthor())
        else:
            self.songName.setText("")
            self.songAuthor.setText("")
            self.player.stop()
            self.bPlay.setIcon(self.iconPlay)
            self.isPlaying = False
        self.labCurrentDuration.setText(
            getStrDuration(self.player.position()))


import os.path
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.Qt import Qt
from util.Config import Config
from .QueueSong import QueueSong
from .PlayerSound import PlayerSound
from .SearchSong import SearchSong


class BoardGUI(QWidget):
    '''
    representation du tableau de bord du lecteur

    :param board: le tableau de bord du lecteur
    :type board: model.Board
    '''

    def __init__(self, board, parent=None):
        QWidget.__init__(self, parent)
        config = Config("config/config.conf")
        self.b = board

        # boolean qui permet d'éviter un double appel par keyPressEvent
        self.changeSong = True

        path = config.getValueOf("path")
        if path and os.path.exists(path):
            self.b.setDirectory(path)
        else:
            config.deleteConfig("path")
            config.save()

        # zone de recherche a gauche
        self.searchSong = SearchSong(self.b)

        # liste d'attente prioritaire
        labPrimary = QLabel("Liste d'attente prioritaire")
        labPrimary.setProperty("class", "title")
        labPrimary.setAlignment(Qt.AlignCenter)
        self.primaryQueue = QueueSong(
            self.b, self.b.getPrimaryQueue, self.b.getSecondaryQueue)

        # liste d'attente secondaire
        labSecondary = QLabel("Liste d'attente")
        labSecondary.setProperty("class", "title")
        labSecondary.setAlignment(Qt.AlignCenter)
        self.secondaryQueue = QueueSong(
            self.b, self.b.getSecondaryQueue, self.b.getPrimaryQueue)

        self.b.addListener(self.primaryQueue)
        self.b.addListener(self.secondaryQueue)

        # partie lecteur en bas
        self.player = PlayerSound(self.b)
        self.b.addListener(self.player)

        # disposition

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
            # suppression de la recherche dans l'input
            self.searchSong.clearSearch()
        if not event.modifiers() & Qt.ControlModifier:
            # si Ctrl n'est pas presse
            if event.key() == Qt.Key_Left:
                # deplacement du focus sur la liste d'attente prioritaire
                self.primaryQueue.setFocus(True)
                index = self.primaryQueue.getIndexSelected()
                if index < 0:
                    # si aucun element n'a ete selectionne jusqu'ici
                    self.primaryQueue.setSelectedIndex(0)
            elif event.key() == Qt.Key_Right:
                # deplacement du focus sur la liste d'attente secondaire
                self.secondaryQueue.setFocus(True)
                index = self.secondaryQueue.getIndexSelected()
                if index < 0:
                    # si aucun element n'a ete selectionne jusqu'ici
                    self.secondaryQueue.setSelectedIndex(0)
        if event.key() == Qt.Key_MediaPlay or event.key() == Qt.Key_MediaPause:
            self.player.play()
        else:
            if self.changeSong:
                # indiquer qu'on est en train de changer la musique
                self.changeSong = False
                if event.key() == Qt.Key_MediaPrevious:
                    self.player.precedentSong()
                elif event.key() == Qt.Key_MediaNext:
                    self.player.nextSong()
                else:
                    # si c'est une autre touche
                    self.changeSong = True
            else:
                # capture d'un du double appel sur l'event Key_MediaPrevious ou Key_MediaNext
                self.changeSong = True

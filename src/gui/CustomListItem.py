
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt5.Qt import Qt
from util.StringDuration import getStrDuration


class CustomListItem(QWidget):
    '''
    ligne customiser d'une QListWidget qui correspond a une musique

    :param song: la musique a representer
    :type song: model.Song
    '''

    def __init__(self, parent=None, song=None):
        super(CustomListItem, self).__init__(parent)
        layout = QHBoxLayout()
        if song:
            self.songName = QLabel(song.getName())
            self.songName.setProperty("class", "bold")
            self.songAuthor = QLabel(song.getAuthor())
            self.songDuration = QLabel(getStrDuration(song.getDuration()))
            self.songDuration.setAlignment(Qt.AlignCenter)
            self.songDuration.setFixedWidth(50)
            layout.addWidget(self.songName)
            layout.addWidget(self.songAuthor)
            layout.addWidget(self.songDuration)
        self.setLayout(layout)

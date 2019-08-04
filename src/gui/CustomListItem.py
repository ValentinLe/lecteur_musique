
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt5.Qt import Qt
from util.StringDuration import getStrDuration


class CustomListItem(QWidget):
    def __init__(self, parent=None, song=None):
        super(CustomListItem, self).__init__(parent)
        layout = QHBoxLayout()
        if song:
            self.songName = QLabel(song.getName())
            self.setFixedWidth(650)
            self.songName.setProperty("class", "bold")
            self.songAuthor = QLabel(song.getAuthor())
            self.songAuthor.setAlignment(Qt.AlignCenter)
            self.songDuration = QLabel(getStrDuration(song.getDuration()))
            self.songDuration.setAlignment(Qt.AlignCenter)
            layout.addWidget(self.songName)
            layout.addWidget(self.songAuthor)
            layout.addWidget(self.songDuration)
        self.setLayout(layout)

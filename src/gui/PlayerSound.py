
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent
from mutagen.id3 import ID3


class PlayerSound(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(QPushButton("test"))

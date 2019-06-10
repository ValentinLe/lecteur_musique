
from PyQt5.QtWidgets import QWidget, QPushButton, QListWidget, QGridLayout
from mutagen.id3 import ID3, ID3NoHeaderError


class QueueSong(QWidget):
    def __init__(self, queue):
        QWidget.__init__(self)

        self.listSong = QListWidget()
        for k in range(queue.size()):
            song = queue.getElementAt(k)
            author = "Unknown"
            try:
                id3 = ID3(
                    "C:/Users/Val/Desktop/Dossier/testLecteur/" + song.getFilename())
                author = id3["TPE1"].text[0]
            except ID3NoHeaderError:
                pass
            self.listSong.addItem(queue.getElementAt(
                k).getName() + " - " + author)

        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.listSong)

    def getIndexSelected(self):
        return self.listSong.currentRow()

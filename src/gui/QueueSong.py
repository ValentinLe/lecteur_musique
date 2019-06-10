
from PyQt5.QtWidgets import QWidget, QPushButton, QListWidget, QGridLayout
from mutagen.id3 import ID3, ID3NoHeaderError


class QueueSong(QWidget):
    def __init__(self, queue):
        QWidget.__init__(self)

        self.queue = queue
        self.listSong = QListWidget()
        self.update()

        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.listSong)

    def getIndexSelected(self):
        return self.listSong.currentRow()

    def update(self):
        self.listSong.clear()
        for k in range(self.queue.size()):
            song = self.queue.getElementAt(k)
            author = "Unknown"
            try:
                id3 = ID3(
                    "C:/Users/Val/Desktop/Dossier/testLecteur/" + song.getFilename())
                author = id3["TPE1"].text[0]
            except ID3NoHeaderError:
                pass
            self.listSong.addItem(self.queue.getElementAt(
                k).getName() + " - " + author)

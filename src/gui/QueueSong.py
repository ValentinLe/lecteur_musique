
from PyQt5.QtWidgets import QWidget, QListWidget, QGridLayout


class QueueSong(QWidget):
    def __init__(self, board, queue, otherQueue):
        QWidget.__init__(self)

        self.board = board
        self.queue = queue
        self.otherQueue = otherQueue
        self.listSong = QListWidget()
        self.update()
        self.listSong.doubleClicked.connect(self.moveSong)

        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.listSong)

    def getIndexSelected(self):
        return self.listSong.currentRow()

    def moveSong(self):
        index = self.getIndexSelected()
        self.board.moveSongOfQueue(self.queue, self.otherQueue, index)

    def update(self):
        self.listSong.clear()
        for k in range(self.queue.size()):
            song = self.queue.getElementAt(k)
            self.listSong.addItem(song.getName() + " - " + song.getAuthor())

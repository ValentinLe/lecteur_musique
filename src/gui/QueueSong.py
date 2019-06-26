
from PyQt5.QtWidgets import QWidget, QListWidget, QGridLayout
from PyQt5.Qt import Qt, QEvent
from util.StringDuration import getStrDuration


class QueueSong(QListWidget):
    def __init__(self, board, queue, otherQueue):
        QListWidget.__init__(self)

        self.board = board
        self.queue = queue
        self.otherQueue = otherQueue
        self.update()
        self.doubleClicked.connect(self.moveSong)

    def getIndexSelected(self):
        return self.currentRow()

    def moveSong(self):
        index = self.getIndexSelected()
        self.board.moveSongOfQueue(self.queue, self.otherQueue, index)

    def keyPressEvent(self, e):
        if e.modifiers() & Qt.ControlModifier:
            indexSelected = self.getIndexSelected()
            indexTarget = indexSelected
            if e.key() == Qt.Key_Up:
                indexTarget -= 1
            elif e.key() == Qt.Key_Down:
                indexTarget += 1

            if indexTarget != indexSelected:
                self.board.switchSong(self.queue, indexSelected, indexTarget)
                self.setCurrentRow(indexSelected)
        QListWidget.keyPressEvent(self, e)

    def update(self):
        self.clear()
        for k in range(self.queue.size()):
            song = self.queue.getElementAt(k)
            self.addItem(
                song.getName() + " - " + song.getAuthor() + " - " + getStrDuration(song.getDuration()))

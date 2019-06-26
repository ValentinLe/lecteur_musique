
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
        indexSelected = self.getIndexSelected()
        if e.key() == Qt.Key_Return:
            self.moveSong()
        if e.modifiers() & Qt.ControlModifier:
            indexTarget = indexSelected
            if e.key() == Qt.Key_Up:
                indexTarget -= 1
            elif e.key() == Qt.Key_Down:
                indexTarget += 1
            if indexTarget != indexSelected:
                self.board.switchSong(self.queue, indexSelected, indexTarget)
            if self.queue == self.board.getPrimaryQueue():
                keyMove = Qt.Key_Right
            else:
                keyMove = Qt.Key_Left
            if e.key() == keyMove:
                self.moveSong()
                if indexSelected + 1 > self.count():
                    indexSelected -= 1
        self.setCurrentRow(indexSelected)
        QListWidget.keyPressEvent(self, e)

    def update(self):
        self.clear()
        for k in range(self.queue.size()):
            song = self.queue.getElementAt(k)
            self.addItem(
                song.getName() + " - " + song.getAuthor() + " - " + getStrDuration(song.getDuration()))

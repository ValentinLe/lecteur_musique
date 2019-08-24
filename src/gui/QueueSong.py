
from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from PyQt5.Qt import Qt
from .CustomListItem import CustomListItem


class QueueSong(QListWidget):
    def __init__(self, board, getterQueue, getterOtherQueue):
        QListWidget.__init__(self)

        self.setProperty("class", "queue")

        self.board = board
        self.getterQueue = getterQueue
        self.getterOtherQueue = getterOtherQueue
        self.queue = getterQueue()
        self.otherQueue = getterOtherQueue()
        self.update()
        self.doubleClicked.connect(self.moveSong)

    def getIndexSelected(self):
        return self.currentRow()

    def setSelectedIndex(self, index):
        self.setCurrentRow(index)

    def moveSong(self):
        index = self.getIndexSelected()
        self.board.moveSongOfQueue(self.queue, self.otherQueue, index)

    def keyPressEvent(self, event):
        indexSelected = self.getIndexSelected()
        if event.key() == Qt.Key_Return:
            self.moveSong()
        if event.modifiers() & Qt.ControlModifier:
            indexTarget = indexSelected
            if event.key() == Qt.Key_Up:
                indexTarget -= 1
            elif event.key() == Qt.Key_Down:
                indexTarget += 1
            if indexTarget != indexSelected and self.queue.isInIndex(indexTarget):
                self.board.switchSong(self.queue, indexSelected, indexTarget)
            if self.queue == self.board.getPrimaryQueue():
                keyMove = Qt.Key_Right
            else:
                keyMove = Qt.Key_Left
            if event.key() == keyMove:
                self.moveSong()
                if indexSelected + 1 > self.count():
                    indexSelected -= 1
            self.setCurrentRow(indexSelected)
            QListWidget.keyPressEvent(self, event)

    def update(self):
        index = self.currentIndex()
        self.clear()
        self.queue = self.getterQueue()
        self.otherQueue = self.getterOtherQueue()
        for k in range(self.queue.size()):
            song = self.queue.getElementAt(k)
            item = CustomListItem(song=song)
            listItem = QListWidgetItem(self)
            listItem.setSizeHint(item.sizeHint())
            self.addItem(listItem)
            self.setItemWidget(listItem, item)
        self.setCurrentIndex(index)

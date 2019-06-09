
from PyQt5.QtWidgets import QWidget, QPushButton, QListWidget, QGridLayout


class QueueSong(QWidget):
    def __init__(self, queue):
        QWidget.__init__(self)

        self.listSong = QListWidget()
        for k in range(queue.size()):
            self.listSong.addItem(queue.getElementAt(k).getName())

        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.listSong)

    def getIndexSelected(self):
        return self.listSong.currentRow()


from PyQt5.QtWidgets import QWidget, QPushButton, QListWidget, QGridLayout


class QueueSong(QWidget):
    def __init__(self, queue):
        QWidget.__init__(self)

        listSong = QListWidget()
        for k in range(queue.size()):
            listSong.addItem(queue.getElementAt(k).getName())

        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(listSong)

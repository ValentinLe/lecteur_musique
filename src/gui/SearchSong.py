
from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout
from .ListSong import ListSong


class SearchSong(QWidget):
    def __init__(self, board):
        QWidget.__init__(self)

        self.board = board

        self.searchBar = QLineEdit()
        self.searchBar.setPlaceholderText("Rechercher...")
        self.searchBar.textChanged.connect(self.textChanged)

        self.listSong = ListSong(self.board)

        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.searchBar)
        layout.addWidget(self.listSong)

    def textChanged(self, event):
        self.listSong.setFilterName(self.searchBar.text().lower())

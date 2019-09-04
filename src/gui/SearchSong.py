
from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout
from PyQt5.Qt import QMargins
from .ListSong import ListSong


class SearchSong(QWidget):
    '''
    zone de recherche de musique

    :param board: le tableau de bord du lecteur
    :type board: model.Board
    '''

    def __init__(self, board):
        QWidget.__init__(self)
        self.board = board

        self.searchBar = QLineEdit()
        self.searchBar.setProperty("class", "searchBar")
        self.searchBar.setPlaceholderText("Rechercher...")
        self.searchBar.textChanged.connect(self.textChanged)

        self.listSong = ListSong(self.board)

        layout = QVBoxLayout()
        # retirer les margins du widget
        layout.setContentsMargins(QMargins(0, 0, 0, 0))

        self.setLayout(layout)
        layout.addWidget(self.searchBar)
        layout.addWidget(self.listSong)

    def textChanged(self, event):
        # on modifie les musiques visible dans la liste sous la barre de recherche
        self.listSong.setFilterName(self.searchBar.text().lower())

    def clearSearch(self):
        self.searchBar.setText("")

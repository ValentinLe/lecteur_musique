
from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from .CustomListItem import CustomListItem


class ListSong(QListWidget):
    '''
    representant la liste des musiques dans l'ordre alphabetique pouvant etre filtrees

    :param board: le tableau de bord du lecteur
    :type board: model.Board
    '''

    def __init__(self, board):
        QListWidget.__init__(self)

        self.setProperty("class", "queue")

        self.board = board
        self.board.addListener(self)
        self.filterName = ""
        self.listFilteredSong = []

        self.doubleClicked.connect(self.addSongToPrimary)
        self.setFilterName(self.filterName)

    def addSongToPrimary(self, event):
        ''' ajoute la musique selectionnee dans la liste prioritaire '''
        index = self.currentRow()
        song = self.listFilteredSong[index]
        self.board.moveSongToPrimary(song)

    def setFilterName(self, filterName):
        self.filterName = filterName
        self.update()

    def update(self):
        self.listFilteredSong = self.board.getOrderListFilterSong(
            self.filterName)
        # on vide la liste des widgets
        self.clear()
        for song in self.listFilteredSong:
            # on la remplie avec les musiques qui ont passees le filtre
            item = CustomListItem(song=song)
            listItem = QListWidgetItem(self)
            listItem.setSizeHint(item.sizeHint())
            self.addItem(listItem)
            self.setItemWidget(listItem, item)

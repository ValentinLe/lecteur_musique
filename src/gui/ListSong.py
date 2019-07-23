
from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from .CustomListItem import CustomListItem


class ListSong(QListWidget):
    def __init__(self, board):
        QListWidget.__init__(self)

        self.setProperty("class", "queue")

        self.board = board
        self.board.addListener(self)
        self.filterName = ""
        self.listFilteredSong = []

        self.doubleClicked.connect(self.addSongToPrimary)

    def getOrderListFilterSong(self):
        listSong = []
        for song in self.board.getPrimaryQueue().getListElements():
            if self.filterName in song.getName().lower():
                listSong.append(song)
        for song in self.board.getSecondaryQueue().getListElements():
            if self.filterName in song.getName().lower():
                listSong.append(song)
        currentSong = self.board.getCurrentSong()
        if self.filterName in currentSong.getName().lower():
            listSong.append(currentSong)
        listSong.sort()
        return listSong

    def addSongToPrimary(self, event):
        index = self.currentRow()
        song = self.listFilteredSong[index]
        self.board.moveSongToPrimary(song)

    def setFilterName(self, filterName):
        self.filterName = filterName
        self.update()

    def update(self):
        self.listFilteredSong = self.getOrderListFilterSong()
        self.clear()
        for song in self.listFilteredSong:
            item = CustomListItem(song=song)
            listItem = QListWidgetItem(self)
            listItem.setSizeHint(item.sizeHint())
            self.addItem(listItem)
            self.setItemWidget(listItem, item)

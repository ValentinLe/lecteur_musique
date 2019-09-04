
from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from PyQt5.Qt import Qt
from .CustomListItem import CustomListItem


class QueueSong(QListWidget):
    '''
    represente une liste d'attente

    :param board: le tableau de bord du lecteur
    :type board: model.Board
    :param getterQueue: le getter de la queue ciblee
    :type getterQueue: function
    :param getterOtherQueue: le getter de l'autre queue
    :type getterOtherQueue: function
    '''

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
            # entrer permet de deplacer la musique de liste
            self.moveSong()
        indexTarget = indexSelected
        if event.key() == Qt.Key_Up:
            # on veut faire un deplacement vers le haut
            indexTarget -= 1
        elif event.key() == Qt.Key_Down:
            # on veut faire un deplacement vers le bas
            indexTarget += 1
        if event.modifiers() & Qt.ControlModifier:
            # si Ctrl est pressee
            if indexTarget != indexSelected and self.queue.isInIndex(indexTarget):
                # si l'echange entre la musique selectionnee et celle voulue (en dessus ou en dessous)
                # est possible
                self.board.switchSong(self.queue, indexSelected, indexTarget)
            if self.queue == self.board.getPrimaryQueue():
                # la liste d'attente represente est la liste prioritaire
                keyMove = Qt.Key_Right
            else:
                # sinon c'est la liste secondaire
                keyMove = Qt.Key_Left
            if event.key() == keyMove:
                # la key de l'event est choisi selon la liste representant par la classe ci-dessus
                self.moveSong()
                if indexSelected > self.count() - 1:
                    # si c'est le dernier element de la liste qui a ete deplace, on change l'indice selectionne
                    indexSelected -= 1
        self.setCurrentRow(indexSelected)
        QListWidget.keyPressEvent(self, event)

    def update(self):
        index = self.currentIndex()
        # on vide la liste de ces widgets
        self.clear()
        # on remet en place les listes
        self.queue = self.getterQueue()
        self.otherQueue = self.getterOtherQueue()
        for k in range(self.queue.size()):
            # remplissage de la liste d'attente par les widgets customs
            song = self.queue.getElementAt(k)
            item = CustomListItem(song=song)
            listItem = QListWidgetItem(self)
            listItem.setSizeHint(item.sizeHint())
            self.addItem(listItem)
            self.setItemWidget(listItem, item)
        self.setCurrentIndex(index)

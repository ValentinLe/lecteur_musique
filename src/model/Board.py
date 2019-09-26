
from mutagen.mp3 import MP3
from util.Queue import Queue
from util.ListFile import listFile
from observer.ListenableModel import ListenableModel
from .Song import Song


class Board(ListenableModel):
    '''
    Classe representant le panneau de gestions d'ordonnancement des musiques
    '''

    def __init__(self):
        ListenableModel.__init__(self)
        self.currentSong = None
        # le repertoire ou se trouvent les musiques
        self.directory = None
        self.primaryQueue = Queue()
        self.secondaryQueue = Queue()

    def getDirectory(self):
        return self.directory

    def setDirectory(self, directory):
        '''
        change le repertoire contenant les musiques

        :param directory: le nouveau repertoire dans lequel lire les musiques
        :type directory: str
        '''
        # on vide les listes d'attentes et la musique courrante
        self.clearSongs()
        # on set le repertoire et on ajoute toutes les musiques qui sont presentes
        self.directory = directory
        self.addSongOfDirectory(directory)
        # on melange et on prend la premiere musique de la liste pour que la musique courante
        # soit differente de None
        self.shuffle(10)
        self.nextSong()

    def addSongOfDirectory(self, directory):
        '''
        ajoute toutes les musiques du repertoire donne au format mp3 dans la liste d'attente

        :param directory: le repertoire dans lequel trouver les musiques
        :type directory: str
        '''
        listFiles = listFile(directory)
        for file in listFiles:
            song = Song(directory, file)
            if song.getFormat() == "mp3":
                # set les infos de la musique (auteur et duree) puis ajout de celle-ci
                audio = MP3(song.getFullFilename())
                song.setDuration(int(audio.info.length * 1000))
                song.setAuthor(audio.tags["TPE1"].text[0])
                self.secondaryQueue.add(song)
        self.firechange()

    def getCurrentSong(self):
        return self.currentSong

    def getPrimaryQueue(self):
        return self.primaryQueue

    def getSecondaryQueue(self):
        return self.secondaryQueue

    def getOrderListFilterSong(self, filterName):
        ''' donne la liste des musiques filtrees ou non dans l'ordre alphabetique '''
        listSong = []
        # si le filtre correspond au nom ou auteur d'une musique de la liste prioritaire
        for song in self.getPrimaryQueue().getListElements():
            if filterName in song.getName().lower() or filterName in song.getAuthor().lower():
                listSong.append(song)
        # si le filtre correspond au nom ou auteur d'une musique de la liste secondaire
        for song in self.getSecondaryQueue().getListElements():
            if filterName in song.getName().lower() or filterName in song.getAuthor().lower():
                listSong.append(song)
        # si le filtre correspond au nom ou auteur de la musique courrante
        if self.currentSong and (filterName in self.currentSong.getName().lower() or
                                 filterName in self.currentSong.getAuthor().lower()):
            listSong.append(self.currentSong)
        listSong.sort()
        return listSong

    def getSongAt(self, queue, index):
        '''
        donne la musique dans la liste d'attente donnee a la position donnee

        :param queue: la liste d'attente dans laquelle on veut la position
        :type queue: util.Queue
        :param index: la position de la musique que l'ont souhaite
        :type index: int
        :return: la musique a la position donnee ou None si la position n'est pas dans l'interval de la liste d'attente
        :rtype: model.Song
        '''
        return queue.getElementAt(index)

    def getSongPrimaryAt(self, index):
        ''' donne la musique de la liste d'attente prioritaire a l'index donnee '''
        return self.getSongAt(self.primaryQueue, index)

    def getSongSecondaryAt(self, index):
        ''' donne la musique de la liste d'attente secondaire a l'index donnee '''
        return self.getSongAt(self.secondaryQueue, index)

    def nextSong(self):
        ''' fait passer a la musique suivante '''
        if self.currentSong:
            self.secondaryQueue.add(self.currentSong)
        if not self.primaryQueue.isEmpty():
            # si la liste d'attente principale n'est pas vide on prend la prochaine musique
            # dans celle si
            self.currentSong = self.primaryQueue.remove()
        else:
            # sinon on prend dans la liste d'attente secondaire
            self.currentSong = self.secondaryQueue.remove()
        self.firechange()
        return self.currentSong

    def precedentSong(self):
        ''' fait passer a la musique precedente '''
        song = self.secondaryQueue.getLast()
        if song:
            if not self.primaryQueue.isEmpty():
                # si la liste prioritaire n'est pas vide on met la musique courrante
                # en debut de celle-ci
                self.primaryQueue.addHead(self.currentSong)
            else:
                # sinon on la met au debut de la liste secondaire
                self.secondaryQueue.addHead(self.currentSong)
            # on retire la musique qui se trouvait avant la musique courrante de la liste
            # d'attente et on la met comme musique courante
            self.secondaryQueue.removeElement(song)
            self.currentSong = song
            self.firechange()

    def moveSongOfQueue(self, startQueue, destQueue, indexStart):
        '''
        deplace une musique d'une liste d'attente et a l'index donnees vers une autre liste d'attente

        :param startQueue: la liste d'attente de depart
        :type startQueue: util.Queue
        :param destQueue: la liste d'attente d'arrivee
        :type destQueue: util.Queue
        :param indexStart: la position de la musique dans la liste d'attente de depart a deplacer
        :type indexStart: int
        '''
        song = startQueue.remove(indexStart)
        if song:
            # si l'index est coherent par rapport aux dimensions de la liste
            destQueue.add(song)
            self.firechange()

    def moveSongOfIndexToPrimary(self, index):
        self.moveSongOfQueue(self.secondaryQueue, self.primaryQueue, index)

    def moveSongOfIndexToSecondary(self, index):
        self.moveSongOfQueue(self.primaryQueue, self.secondaryQueue, index)

    def moveSongToPrimary(self, song):
        '''
        deplace la musique donnee dans la liste d'attente prioritaire

        :param song: la musique a deplacer
        :type song: model.Song
        '''
        if song in self.secondaryQueue:
            self.secondaryQueue.removeElement(song)
            self.primaryQueue.add(song)
            self.firechange()

    def switchSong(self, queue, firstIndex, secondIndex):
        '''
        echange la position entre deux musique dans une liste d'attente

        :param queue: la liste d'attente dans laquelle faire l'echange
        :type queue: util.Queue
        :param firstIndex: la position de la premiere musique a echanger
        :type firstIndex: int
        :param secondIndex: la position de la deuxieme musique a echanger
        :type secondIndex: int
        '''
        queue.switchElements(firstIndex, secondIndex)
        self.firechange()

    def shuffle(self, nb=1):
        ''' melange la liste d'attente secondaire '''
        self.secondaryQueue.shuffle(nb)
        self.firechange()

    def clearSongs(self):
        ''' vide les liste d'attentes et retire la musique courrante '''
        self.currentSong = None
        self.primaryQueue = Queue()
        self.secondaryQueue = Queue()

    def __repr__(self):
        return "Board :\ncurrent=" + str(self.currentSong) + "\nprimary : \n" + str(self.primaryQueue) + "\n\nsecondary : \n" + str(self.secondaryQueue)

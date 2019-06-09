
from util.Queue import Queue
from util.ListFile import listFile
from .Song import Song


class Board():
    def __init__(self):
        self.currentSong = None
        self.primaryQueue = Queue()
        self.secondaryQueue = Queue()

    def addSongOfDirectory(self, directory):
        listFiles = listFile(directory)
        for file in listFiles:
            song = Song(file)
            self.secondaryQueue.add(song)

    def getPrimaryQueue(self):
        return self.primaryQueue

    def getSecondaryQueue(self):
        return self.secondaryQueue

    def _getSongAt(self, queue, index):
        return queue.getElementAt(index)

    def getSongPrimaryAt(self, index):
        return self._getSongAt(self.primaryQueue, index)

    def getSongSecondaryAt(self, index):
        return self._getSongAt(self.secondaryQueue, index)

    def nextSong(self):
        if self.currentSong:
            self.secondaryQueue.add(self.currentSong)
        if not self.primaryQueue.isEmpty():
            self.currentSong = self.primaryQueue.remove()
        else:
            self.currentSong = self.secondaryQueue.remove()

    def _moveSongOfQueue(self, startQueue, destQueue, indexStart):
        song = startQueue.remove(indexStart)
        if song:
            destQueue.add(song)

    def moveSongToPrimary(self, index):
        self._moveSongOfQueue(self.secondaryQueue, self.primaryQueue, index)

    def __repr__(self):
        return "Board :\ncurrent=" + str(self.currentSong) + "\nprimary : \n" + str(self.primaryQueue) + "\n\nsecondary : \n" + str(self.secondaryQueue)


from mutagen.mp3 import MP3
from util.Queue import Queue
from util.ListFile import listFile
from observer.ListenableModel import ListenableModel
from .Song import Song


class Board(ListenableModel):
    def __init__(self):
        ListenableModel.__init__(self)
        self.currentSong = None
        self.primaryQueue = Queue()
        self.secondaryQueue = Queue()

    def addSongOfDirectory(self, directory):
        listFiles = listFile(directory)
        for file in listFiles:
            song = Song(directory, file)
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

    def getSongAt(self, queue, index):
        return queue.getElementAt(index)

    def getSongPrimaryAt(self, index):
        return self.getSongAt(self.primaryQueue, index)

    def getSongSecondaryAt(self, index):
        return self.getSongAt(self.secondaryQueue, index)

    def nextSong(self):
        if self.currentSong:
            self.secondaryQueue.add(self.currentSong)
        if not self.primaryQueue.isEmpty():
            self.currentSong = self.primaryQueue.remove()
        else:
            self.currentSong = self.secondaryQueue.remove()
        self.firechange()
        return self.currentSong

    def moveSongOfQueue(self, startQueue, destQueue, indexStart):
        song = startQueue.remove(indexStart)
        if song:

            destQueue.add(song)
            self.firechange()

    def moveSongToPrimary(self, index):
        self.moveSongOfQueue(self.secondaryQueue, self.primaryQueue, index)

    def moveSongToSecondary(self, index):
        self.moveSongOfQueue(self.primaryQueue, self.secondaryQueue, index)

    def __repr__(self):
        return "Board :\ncurrent=" + str(self.currentSong) + "\nprimary : \n" + str(self.primaryQueue) + "\n\nsecondary : \n" + str(self.secondaryQueue)

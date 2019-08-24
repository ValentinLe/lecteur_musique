
from mutagen.mp3 import MP3
from util.Queue import Queue
from util.ListFile import listFile
from observer.ListenableModel import ListenableModel
from .Song import Song


class Board(ListenableModel):
    def __init__(self):
        ListenableModel.__init__(self)
        self.currentSong = None
        self.directory = None
        self.primaryQueue = Queue()
        self.secondaryQueue = Queue()

    def getDirectory(self):
        return self.directory

    def setDirectory(self, directory):
        self.clearSongs()
        self.directory = directory
        self.addSongOfDirectory(directory)
        self.shuffle(10)

    def addSongOfDirectory(self, directory):
        listFiles = listFile(directory)
        for file in listFiles:
            song = Song(directory, file)
            if song.getFormat() == "mp3":
                audio = MP3(song.getFullFilename())
                song.setDuration(int(audio.info.length * 1000))
                song.setAuthor(audio.tags["TPE1"].text[0])
                self.secondaryQueue.add(song)
        self.nextSong()
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

    def precedentSong(self):
        song = self.secondaryQueue.getLast()
        if song:
            if not self.primaryQueue.isEmpty():
                self.primaryQueue.addHead(self.currentSong)
            else:
                self.secondaryQueue.addHead(self.currentSong)
            self.secondaryQueue.removeElement(song)
            self.currentSong = song
            self.firechange()

    def moveSongOfQueue(self, startQueue, destQueue, indexStart):
        song = startQueue.remove(indexStart)
        if song:
            destQueue.add(song)
            self.firechange()

    def moveSongOfIndexToPrimary(self, index):
        self.moveSongOfQueue(self.secondaryQueue, self.primaryQueue, index)

    def moveSongOfIndexToSecondary(self, index):
        self.moveSongOfQueue(self.primaryQueue, self.secondaryQueue, index)

    def moveSongToPrimary(self, song):
        if song in self.secondaryQueue:
            self.secondaryQueue.removeElement(song)
            self.primaryQueue.add(song)
            self.firechange()

    def switchSong(self, queue, firstIndex, secondIndex):
        queue.switchElements(firstIndex, secondIndex)
        self.firechange()

    def shuffle(self, nb=1):
        self.secondaryQueue.shuffle(nb)
        self.firechange()

    def clearSongs(self):
        self.currentSong = None
        self.primaryQueue = Queue()
        self.secondaryQueue = Queue()

    def __repr__(self):
        return "Board :\ncurrent=" + str(self.currentSong) + "\nprimary : \n" + str(self.primaryQueue) + "\n\nsecondary : \n" + str(self.secondaryQueue)


import random


class Queue():
    def __init__(self):
        self.queue = []
        self.length = 0

    def add(self, elt):
        self.queue.append(elt)
        self.length += 1

    def getElementAt(self, index):
        if self.isInIndex(index):
            return self.queue[index]
        return None

    def isEmpty(self):
        return self.length == 0

    def isInIndex(self, index):
        return index >= 0 and index < self.length

    def remove(self, index=0):
        elt = None
        if not self.isEmpty() and self.isInIndex(index):
            elt = self.getElementAt(index)
            del self.queue[index]
            self.length -= 1
        return elt

    def setElementAt(self, element, index):
        if self.isInIndex(index):
            self.queue[index] = element

    def size(self):
        return self.length

    def shuffle(self, nb=1):
        i = 0
        while i < nb:
            random.shuffle(self.queue)
            i += 1

    def switchElements(self, firstIndex, secondIndex):
        firstElement = self.getElementAt(firstIndex)
        secondElement = self.getElementAt(secondIndex)
        self.setElementAt(secondElement, firstIndex)
        self.setElementAt(firstElement, secondIndex)

    def __repr__(self):
        return "Queue, size = " + str(self.length) + "\n" + str(self.queue)

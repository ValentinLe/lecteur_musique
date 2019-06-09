
import random


class Queue():
    def __init__(self):
        self.queue = []
        self.length = 0

    def add(self, elt):
        self.queue.append(elt)
        self.length += 1

    def remove(self):
        elt = None
        if self.length > 0:
            elt = self.queue[0]
            del self.queue[0]
            self.length -= 1
        return elt

    def size(self):
        return self.length

    def shuffle(self, nb=1):
        i = 0
        while i < nb:
            random.shuffle(self.queue)
            i += 1

    def __repr__(self):
        return "Queue, size = " + str(self.length) + "\n" + str(self.queue)


class Song():
    def __init__(self, filename):
        self.filename = filename

    def getFilename(self):
        return self.filename

    def __repr__(self):
        return "Song : " + self.filename

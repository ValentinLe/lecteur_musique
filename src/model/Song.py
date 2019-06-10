
class Song():
    def __init__(self, path, filename, author="Unknown"):
        self.path = path
        self.filename = filename
        self.name = filename.split(".")[0]
        self.format = filename.split(".")[1]
        self.author = author

    def getAuthor(self):
        return self.author

    def getFullFilename(self):
        return self.path + "/" + self.filename

    def getFilename(self):
        return self.filename

    def getName(self):
        return self.name

    def getFormat(self):
        return self.format

    def setAuthor(self, author):
        self.author = author

    def __eq__(self, other):
        return self.filename == other.getFilename()

    def __repr__(self):
        return "<_" + self.filename + "_>"

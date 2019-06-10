
class Song():
    def __init__(self, path, filename):
        self.path = path
        self.filename = filename
        self.name = filename.split(".")[0]
        self.format = filename.split(".")[1]

    def getFullFilename(self):
        return self.path + "/" + self.filename

    def getFilename(self):
        return self.filename

    def getName(self):
        return self.name

    def getFormat(self):
        return self.format

    def __eq__(self, other):
        return self.filename == other.getFilename()

    def __repr__(self):
        return "<_" + self.filename + "_>"

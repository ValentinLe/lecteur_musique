
from os import listdir
from os.path import isfile, join


def listFile(path):
    listFiles = []
    for elt in listdir(path):
        if isfile(join(path, elt)):
            listFiles.append(elt)
    return listFiles

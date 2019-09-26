
from os import listdir
from os.path import isfile, join


def listFile(path):
    '''
    liste les fichiers d'un dossier donnee
    :param path: le dossier dans lequel lister les fichiers
    :type path: str
    :return: la liste des noms des fichiers presents
    :rtype: list
    '''
    listFiles = []
    for elt in listdir(path):
        if isfile(join(path, elt)):
            listFiles.append(elt)
    return listFiles

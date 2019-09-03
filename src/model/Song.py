
class Song():
    '''
    Classe representant une musique

    :param path: le chemin du dossier dans lequel trouver la musique
    :type path: str
    :param filename: le nom du fichier dans le dossier ou il se trouve (sans le chemin)
    :type filename: str
    :param author: l'auteur de la musique
    :type author: str
    :param duration: la duree en ms de la musique
    :type duration: int
    '''

    def __init__(self, path, filename, author="Unknown", duration=0):
        self.path = path
        self.filename = filename
        self.format = filename.split(".")[-1]
        self.name = filename.split("." + str(self.format))[0]
        self.author = author
        self.duration = duration

    def getAuthor(self):
        '''
        getter sur l'auteur de la musique

        :return: l'auteur de la musique
        :rtype: str
        '''
        return self.author

    def getFullFilename(self):
        '''
        donne le chemin absolu de la musique

        :return: le nom complet de la musique
        :rtype: str
        '''
        return self.path + "/" + self.filename

    def getFilename(self):
        '''
        donne le nom du fichier de la musique

        :return: le nom du fichier
        :rtype: str
        '''
        return self.filename

    def getName(self):
        '''
        donne le nom de la musique

        :return: le nom de la musique
        :rtype: str
        '''
        return self.name

    def getFormat(self):
        '''
        donne le format du fichier de la musique

        :return: le format du fichier
        :rtype: str
        '''
        return self.format

    def getDuration(self):
        '''
        donne la duree en ms de la musique

        :return: la duree en ms de la musique
        :rtype: int
        '''
        return self.duration

    def setAuthor(self, author):
        '''
        setter sur l'auteur de la musique

        :param author: l'auteur à setter à la musique
        :type author: str
        '''
        self.author = author

    def setDuration(self, duration):
        '''
        setter sur la duree de la musique

        :param duration: la duree à setter à la musique
        :type duration: int
        '''
        self.duration = duration

    def __eq__(self, other):
        '''
        deux musiques sont egales si elles ont le meme nom de fichier complet

        :param other: l'autre musique pour le test d'egalite
        :type other: model.Song
        '''
        return self.getFullFilename() == other.getFullFilename()

    def __lt__(self, other):
        '''
        une musique est consideree plus petite qu'une autre si son nom est plus petit que l'autre

        :param other: l'autre musique pour la comparaison
        :type other: model.Song
        '''
        return self.name < other.getName()

    def __repr__(self):
        return "<_" + self.filename + "_>"

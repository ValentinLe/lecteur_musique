
class ListenableModel():
    '''
    Classe permettant a un model d'etre ecouter par les ecouteurs
    '''

    def __init__(self):
        self.listeners = []

    def addListener(self, modelListener):
        '''
        ajoute un ecouteur au model

        :param modelListener: l'ecouteur a ajouter pour ecouter le model
        :type modelListener: observer.ModelListener
        '''
        self.listeners.append(modelListener)

    def removeListener(self, modelListener):
        '''
        supprime un ecouteur au model

        :param modelListener: l'ecouteur a retirer du model
        :type observeur.ModelListener
        '''
        self.listeners.remove(modelListener)

    def firechange(self):
        '''
        indique a tous les ecouteurs du model qu'il s'est passe quelque chose
        '''
        for listener in self.listeners:
            listener.update()

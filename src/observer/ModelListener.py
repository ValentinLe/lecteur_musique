
class ModelListener():
    '''
    Classe qui servira pour les ecouteurs du model afin qu'ils puissent se mettre a jour
    '''

    def update(self):
        '''
        indique a l'ecouteur que quelque chose s'est passe dans le model
        '''
        raise NotImplementedError("method \"update\" isn't implemented")

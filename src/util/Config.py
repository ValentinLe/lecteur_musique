
class Config():
    '''
    Classe representant l'ensembles des configurations
    '''

    def __init__(self, configFile):
        self.configFile = configFile
        self.configMap = self.findConfig({})

    def findConfig(self, configMap):
        '''
        permet de mettre toutes les configurations dans la map donnee

        :param configMap: la map de l'ensemble des configurations
        :type configMap: dict
        :return: la map des configurations remplie
        :rtype: dict
        '''
        file = open(self.configFile, "r")
        for line in file:
            couple = line.split("=")
            configMap[couple[0]] = couple[1]
        file.close()
        return configMap

    def getValueOf(self, configName):
        '''
        donne la valeur de la configuration donnee

        :param configName: la configuration dont on veut la valeur
        :type configName: str
        :return: la valeur de la configuration
        :rtype: str
        '''
        if configName in self.configMap:
            return self.configMap[configName]
        else:
            return None

    def setValueOf(self, configName, value):
        '''
        change la valeur de la configuration donnee

        :param configName: le nom de la configuration a changer
        :type configName: str
        :param value: la valeur a affecter a la configuration
        :type value: str
        '''
        self.configMap[configName] = value

    def deleteConfig(self, configName):
        ''' supprime une config donnee '''
        if configName in self.configMap:
            del self.configMap[configName]

    def save(self):
        ''' permet de sauvegarder les configurations dans son fichier '''
        file = open(self.configFile, "w")
        res = ""
        separator = "="
        for config in self.configMap:
            res += config + separator + self.getValueOf(config)
        file.write(res)
        file.close()

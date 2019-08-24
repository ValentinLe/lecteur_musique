
class Config():
    def __init__(self, configFile):
        self.configFile = configFile
        self.configMap = self.findConfig({})

    def findConfig(self, configMap):
        file = open(self.configFile, "r")
        for line in file:
            couple = line.split("=")
            configMap[couple[0]] = couple[1]
        file.close()
        return configMap

    def getValueOf(self, configName):
        return self.configMap[configName]

    def setValueOf(self, configName, value):
        self.configMap[configName] = value

    def save(self):
        file = open(self.configFile, "w")
        res = ""
        separator = "="
        for config in self.configMap:
            res += config + separator + self.getValueOf(config)
        file.write(res)
        file.close()

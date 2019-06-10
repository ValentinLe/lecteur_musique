
class ListenableModel():
    def __init__(self):
        self.listeners = []

    def addListener(self, modelListener):
        self.listeners.append(modelListener)

    def removeListener(self, modelListener):
        self.listeners.remove(modelListener)

    def firechange(self):
        for listener in self.listeners:
            listener.update()

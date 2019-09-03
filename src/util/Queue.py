
import random


class Queue():
    '''
    Classe representant un liste d'attente
    '''

    def __init__(self):
        self.queue = []
        self.length = 0

    def add(self, elt):
        '''
        ajoute un element a la liste d'attente

        :param elt: l'element a ajouter
        :type elt: Object
        '''
        self.queue.append(elt)
        self.length += 1

    def getElementAt(self, index):
        '''
        donne l'element a la position donnee

        :param index: la position de l'element qu'on souhaite
        :type index: int
        :return: l'element a la position donnee ou None si la position n'est pas dans l'intervalle de la liste
        d'attente
        :rtype: Object
        '''
        if self.isInIndex(index):
            return self.queue[index]
        return None

    def getListElements(self):
        '''
        getter sur la liste de la liste d'attente

        :return: la liste des elements de la liste d'attente
        :rtype: list
        '''
        return self.queue

    def addHead(self, element):
        '''
        ajoute un element en tete de la liste d'attente

        :param element: l'element a ajouter en tete de la liste
        :type element: Object
        '''
        self.queue.insert(0, element)
        self.length += 1

    def isEmpty(self):
        '''
        test si la liste est vide
        :return: True si la liste est vide, False sinon
        :rtype: bool
        '''
        return self.length == 0

    def isInIndex(self, index):
        '''
        test si l'index donnee est dans l'interval de la liste d'attente

        :param index: la position a tester
        :type index: int
        :return: True si l'index est entre 0 et la taille de la liste, False sinon
        :rtype: bool
        '''
        return index >= 0 and index < self.length

    def getLast(self):
        '''
        donne le dernier element de la liste d'attente ou None si la liste est vide

        :return: le dernier element de la liste d'attente ou None si la liste est vide
        :rtype: Object
        '''
        if not self.isEmpty():
            return self.queue[-1]
        else:
            return None

    def remove(self, index=0):
        '''
        supprime l'element a l'index donnee, si l'index n'est pas fourni, le premier element sera supprime

        :param index: la position de l'element a supprimer de la liste
        :rtype: int
        :return: l'element qui a etait supprime
        :rtype: Object
        '''
        elt = None
        if not self.isEmpty() and self.isInIndex(index):
            elt = self.getElementAt(index)
            del self.queue[index]
            self.length -= 1
        return elt

    def removeElement(self, element):
        '''
        supprime l'element donnee de la liste si il existe

        :param element: l'element a supprime
        :type element: Object
        :return: True si l'element a etait supprime, False si il n'est pas dans la liste
        :rtype: bool
        '''
        if element in self.queue:
            self.queue.remove(element)
            self.length -= 1
            return True
        else:
            return False

    def setElementAt(self, element, index):
        '''
        set l'element a la position donnee si elle est coherente

        :param element: l'element a setter
        :type element: Object
        :param index: la position a laquelle setter l'element
        :type index: int
        '''
        if self.isInIndex(index):
            self.queue[index] = element

    def size(self):
        '''
        donne la taille de la liste d'attente

        :return: la taille de la liste d'attente
        :rtype: int
        '''
        return self.length

    def shuffle(self, nb=1):
        '''
        melange un certain nombre de fois la liste d'attente

        :param nb: le nombre de fois que la liste d'attente doit etre melangee
        :type nb: int
        '''
        i = 0
        while i < nb:
            random.shuffle(self.queue)
            i += 1

    def switchElements(self, firstIndex, secondIndex):
        '''
        echange la position de deux element de la liste

        :param firstIndex: la position du premier element a echanger
        :type firstIndex: int
        :param secondIndex: la position du second element a echanger
        :type secondIndex: int
        '''
        firstElement = self.getElementAt(firstIndex)
        secondElement = self.getElementAt(secondIndex)
        self.setElementAt(secondElement, firstIndex)
        self.setElementAt(firstElement, secondIndex)

    def __contains__(self, element):
        for elt in self.queue:
            if element == elt:
                return True
        return False

    def __repr__(self):
        return "Queue, size = " + str(self.length) + "\n" + str(self.queue)

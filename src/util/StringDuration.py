
def getStrDuration(millis):
    '''
    donne la representation sous forme de string d'un temps en millisecondes
    ex: 248546 -> 4:08
    '''
    secondes = millis // 1000
    minutes = secondes // 60
    secondes = secondes % 60
    res = str(minutes) + ":"
    if secondes < 10:
        res += "0"
    res += str(secondes)
    return res

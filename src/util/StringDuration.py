
def getStrDuration(millis):
    secondes = millis // 1000
    minutes = secondes // 60
    secondes = secondes % 60
    res = str(minutes) + ":"
    if secondes < 10:
        res += "0"
    res += str(secondes)
    return res

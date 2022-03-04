class Stol():

    def __init__(self):
        self.__gracze = []
        self.__talia = []
        self.__pula = 0

    def dodajGracza(self, nowyGracz):
        self.__gracze.append(nowyGracz)

    def getGracze(self):
        return self.__gracze

    def __str__(self):
        return """Reprezentacja stółu do pokera"""

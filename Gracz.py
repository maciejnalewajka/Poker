class Gracz():

    def __init__(self):
        self.__karty = []
        self.__imie = ""
        self.__pieniadze = 0

    def setImie(self, noweImie):
        self.__imie = noweImie

    def getPieniadze(self):
        #Pieniądze jeszcze są
        if self.__pieniadze != 0:
            self.__pieniadze -= 1
            return 1
        #Pieniądze się skończyły
        return 0
        
    def dodajPieniadze(self, wygranePieniadze):
        self.__pieniadze += wygranePieniadze

    def setKarty(self, karty):
        self.__karty = karty

    def getKarty(self):
        return self.__karty

    def __str__(self):
        return """Reprezentacja gracza"""

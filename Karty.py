class Karta():

    def __init__(self):
        self.__kolor = 0
        self.__wartosc = 0

    def setKolor(self, kolor):
        self.__kolor = kolor

    def getKolor(self):
        return self.__kolor

    def setWartosc(self, wartosc):
        self.__wartosc = wartosc

    def getWartosc(self):
        return self.__wartosc

    def __str__(self):
        return """Reprezentacja jednej karty. Zawiera kolor i wartość."""

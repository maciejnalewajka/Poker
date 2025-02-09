"""---------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 09/02/2025.
    Version: 1.001
    Copyright © 2024 Maciej Nalewajka. All rights reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

class Karta:

    def __init__(self, kolor = 0, wartosc = 0):
        self.__kolor = kolor
        self.__wartosc = wartosc

    def setKolor(self, kolor):
        self.__kolor = kolor

    def getKolor(self) -> int:
        return self.__kolor

    def setWartosc(self, wartosc):
        self.__wartosc = wartosc

    def getWartosc(self) -> int:
        return self.__wartosc

    def __str__(self):
        return """Reprezentacja karty."""

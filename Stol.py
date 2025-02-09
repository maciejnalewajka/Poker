"""---------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 09/02/2025.
    Version: 1.001
    Copyright © 2024 Maciej Nalewajka. All rights reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

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

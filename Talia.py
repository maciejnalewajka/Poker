"""---------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 09/02/2025.
    Version: 1.001
    Copyright © 2024 Maciej Nalewajka. All rights reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

class Talia():

    def __init__(self):
        self.__talia = []

    def setTalia(self, talia):
        self.__talia = talia

    def getTalia(self):
        return self.__talia

    def __str__(self):
        return """Reprezentacja talii kart"""

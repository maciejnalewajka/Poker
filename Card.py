"""---------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 09/02/2025.
    Version: 1.001
    Copyright © 2024 Maciej Nalewajka. All rights reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

class Card:

    def __init__(self, color = 0, value = 0):
        self.__color = color
        self.__value = value

    def setColor(self, color):
        "Set card color"
        self.__color = color

    def getColor(self) -> int:
        "Get card color"
        return self.__color

    def setValue(self, value):
        "Set card value"
        self.__value = value

    def getValue(self) -> int:
        "Get card value"
        return self.__value

    def __str__(self):
        return """Card representation."""

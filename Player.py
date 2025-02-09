"""---------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 09/02/2025.
    Version: 1.001
    Copyright © 2024 Maciej Nalewajka. All rights reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

class Player():

    def __init__(self, money=0):
        self.__cards = []
        self.__name = ""
        self.__money = money

    def __str__(self):
        return str("Player " + self.__name)

    def setName(self, newName):
        "Set player name. Shall be used before __str__()"
        self.__name = newName

    def addMoney(self, money):
        "Add money to the table"
        if self.__money - money >= 0:
            self.__money -= money
            return money        #Money still are
        return 0        #No more money
        
    def getMoney(self, winMoney):
        "Take win money from the table"
        self.__money += winMoney

    def getCards(self, cards):
        "Get cards from the table"
        self.__cards = cards

    def setCards(self):
        "Set cards to the table"
        return self.__cards
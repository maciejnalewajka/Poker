"""---------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 09/02/2025.
    Version: 1.001
    Copyright © 2024 Maciej Nalewajka. All rights reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

class Table():

    def __init__(self):
        self.__players = []
        self.__deckOfCards = []
        self.__moneyInTable = 0

    def addPlayer(self, newPlayer):
        "Add new player"
        self.__players.append(newPlayer)

    def getPlayers(self):
        "Get poker players"
        return self.__players

    def __str__(self):
        return """Poker Table"""

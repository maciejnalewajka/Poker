"""---------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 09/02/2025.
    Version: 1.001
    Copyright © 2024 Maciej Nalewajka. All rights reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

class DeckOfCards():

    def __init__(self):
        self.__deckOfCards = []

    def setDeckOfCards(self, deckOfCards):
        "Set deck of cards"
        self.__deckOfCards = deckOfCards

    def getDeckOfCards(self):
        "Get deck of cards"
        return self.__deckOfCards

    def __str__(self):
        return """Deck of cards"""

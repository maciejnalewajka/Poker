"""---------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 09/02/2025.
    Version: 1.001
    Copyright © 2024 Maciej Nalewajka. All rights reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

import Card as C
from typing import Optional

class PokerHands:

    def __str__(self):
        return """Poker hands representation"""

    def __isRoyalFlush(self, cards:C) -> bool:
        "Royal Flush"
        _sumValue = 60
        _color = cards[0].getColor()
        for i in cards:
            if i.getColor() != _color:
                return False
            _sumValue -= i.getValue()
        if _sumValue != 0:
            return False
        return True

    def __isStraightFlush(self, cards:C) -> bool:
        "Straight Flush"
        _listSumValues = [20, 25, 30, 35, 40, 45, 50, 55]
        _value = 0
        _color = cards[0].getColor()
        for i in cards:
            if i.getColor() != _color:
                return False
            _value += i.getValue()
        if _value not in _listSumValues:
            return False
        return True

    def __isFourOfaKind(self, cards:C) -> bool:
        "Four of a Kind"
        if self.__isFourOfaKindOrisFullHouse(cards) == 2:
            return True
        return False

    def __isFullHouse(self, cards:C) -> bool:
        "Full House"
        if self.__isFourOfaKindOrisFullHouse(cards) == 1:
            return True
        return False

    def __isFourOfaKindOrisFullHouse(self, cards:C):
        __kardsDict = {}
        for i in cards:
            if i.getValue() not in __kardsDict:
                __kardsDict[i.getValue()] = 1
            else:
                __kardsDict[i.getValue()] = __kardsDict.get(i.getValue()) + 1
        if len(__kardsDict) < 3:
            if __kardsDict.get(cards[0].getValue()) in (3, 2):
                return 1
            elif __kardsDict.get(cards[0].getValue()) in (4, 1):
                return 2
        print(__kardsDict)
        return 0

    def __isFlush(self, cards:C) -> bool:
        "Flush"
        _color = cards[0].getColor()
        for i in cards:
            if i.getColor() != _color:
                return False
        return True

    def __isStraight(self, cards:C) -> bool:
        "Straight"
        _listSumValues = [20, 25, 30, 35, 40, 45, 50, 55, 60]
        _value = 0
        for i in cards:
            _value += i.getValue()
        if _value not in _listSumValues:
            return False
        return True

    def __isThreeOfaKind(self, cards:C) -> bool:
        "Three of a Kind"
        if self.__isThreeOfaKindOrisTwoPairOrisOnePair(cards) == 3:
            return True
        return False

    def __isTwoPair(self, cards:C) -> bool:
        "Two Pair"
        if self.__isThreeOfaKindOrisTwoPairOrisOnePair(cards) == 2:
            return True
        return False

    def __isOnePair(self, cards:C) -> bool:
        "One Pair"
        if self.__isThreeOfaKindOrisTwoPairOrisOnePair(cards) == 1:
            return True
        return False

    def __isThreeOfaKindOrisTwoPairOrisOnePair(self, cards:C):
        #TODO
        pass

    def checkPokerHands(self, cards:C) -> int:
        "Check poker hands"
        if __isRoyalFlush(cards):
            return 1
        elif __isStraightFlush(cards):
            return 2
        elif __isFourOfaKind(cards):
            return 3
        elif __isFullHouse(cards):
            return 4
        elif __isFlush(cards):
            return 5
        elif __isStraight(cards):
            return 6
        elif __isThreeOfaKind(cards):
            return 7
        elif __isTwoPair(cards):
            return 8
        elif __isOnePair(cards):
            return 9
        else:
            return 0
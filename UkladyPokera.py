"""---------------------------------------------------------------------------------------------------------------------------------------------------
    Author: Maciej Nalewajka
    Edit Date: 09/02/2025.
    Version: 1.001
    Copyright © 2024 Maciej Nalewajka. All rights reserved.
----------------------------------------------------------------------------------------------------------------------------------------------------"""

import Karta as k
from typing import Optional

class UkladyPokera:

    def czyPokerKrolewski(self, karty) -> bool:
        """Poker królewski"""
        _sumaWartosci = 60
        _kolor = karty[0].getKolor()
        for i in karty:
            if i.getKolor() != _kolor:
                return False
            _sumaWartosci -= i.getWartosc()
        if _sumaWartosci != 0:
            return False
        return True

    def czyPoker(self, karty) -> bool:
        """Zwykły Poker"""
        _listaSumaWartosci = [20, 25, 30, 35, 40, 45, 50, 55]
        _wartosc = 0
        _kolor = karty[0].getKolor()
        for i in karty:
            if i.getKolor() != _kolor:
                return False
            _wartosc += i.getWartosc()
        if _wartosc not in _listaSumaWartosci:
            return False
        return True

    def czyKareta(self, karty) -> bool:
        if self.__karetaCzyFul(karty) == 2:
            return True
        return False

    def czyFul(self, karty) -> bool:
        if self.__karetaCzyFul(karty) == 1:
            return True
        return False

    def __karetaCzyFul(self, karty):
        __slownikKart = {}
        for i in karty:
            if i.getWartosc() not in __slownikKart:
                __slownikKart[i.getWartosc()] = 1
            else:
                __slownikKart[i.getWartosc()] = __slownikKart.get(i.getWartosc()) + 1
        if len(__slownikKart) < 3:
            if __slownikKart.get(karty[0].getWartosc()) in (3, 2):
                return 1
            elif __slownikKart.get(karty[0].getWartosc()) in (4, 1):
                return 2
        print(__slownikKart)
        return 0

    def czyKolor(self, karty) -> bool:
        _kolor = karty[0].getKolor()
        for i in karty:
            if i.getKolor() != _kolor:
                return False
        return True

    def czyStrit(self, karty) -> bool:
        _listaSumaWartosci = [20, 25, 30, 35, 40, 45, 50, 55, 60]
        _wartosc = 0
        for i in karty:
            _wartosc += i.getWartosc()
        if _wartosc not in _listaSumaWartosci:
            return False
        return True

    def czyTrojka(self, karty) -> bool:
        if self.__trojkaParyDwojka(karty) == 3:
            return True
        return False

    def czyPara(self, karty) -> bool:
        if self.__trojkaParyDwojka(karty) == 2:
            return True
        return False

    def czyDwojka(self, karty) -> bool:
        if self.__trojkaParyDwojka(karty) == 1:
            return True
        return False

    def __trojkaParyDwojka(self, karty):
        pass

    def __str__(self):
        return """Reprezentacja układów Pokera. Posiada funkcje sprawdzające układy"""

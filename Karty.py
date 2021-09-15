
class Karty():
    def __init__(self):
        self.lista_kart = self.__uzupelnij_liste()

    @staticmethod
    def __uzupelnij_liste():
        kolory = ["Pik", "Trefl", "Kier", "Karo"]
        lista_kart = []
        for kolor in kolory:
            for i in range(1, 14):
                lista_kart.append(Karta(kolor, i))
        return lista_kart



class Karta():
    def __init__(self, kolor, wartosc):
        self.kolor = kolor
        self.wartosc = wartosc
a = Karty()

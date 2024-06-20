class Karta:
    def __init__(self, rodzaj_fasolki: str, wartosc: list[int], ilosc: int):
        if len(wartosc) != 5:
            raise ValueError("Wartosc musi być listą piecioelementową.")
        self.rodzaj_fasolki = rodzaj_fasolki
        self.wartosc = wartosc
        self.ilosc = ilosc

    def get_rodzaj_fasolki(self) -> str:
        return self.rodzaj_fasolki

    def get_wartosc(self) -> list[int]:
        return self.wartosc

    def get_ilosc(self) -> int:
        return self.ilosc

    def set_ilosc(self, nowa_ilosc: int):
        self.ilosc = nowa_ilosc

    '''
    def __str__(self) -> str:
        wartosc_str = ', '.join([f"{i}: {v}" for i, v in enumerate(self.wartosc)])
        return f"Karta{{rodzaj_fasolki='{self.rodzaj_fasolki}', wartosc={{ {wartosc_str} }}, ilosc={self.ilosc}}}"
    '''

    def __str__(self) -> str:
        return f"Karta{{'{self.rodzaj_fasolki}'}}"

#test
'''
if __name__ == "__main__":
    wartosc = [0, 0, 2, 3, 0]    # Przykładowa wartość: 0 moneta za 0/1 fasolek, 2 monety za 2 fasolki, 3 za 3 fasolki 0 za 4
    karta = Karta("Ogrodnik", wartosc, 6)
    print(karta)
    print("Rodzaj fasolki:", karta.get_rodzaj_fasolki())
    print("Wartość:", karta.get_wartosc())
    print("Ilość:", karta.get_ilosc())
    karta.set_ilosc(10)
    print("Zaktualizowana ilość:", karta.get_ilosc())
'''
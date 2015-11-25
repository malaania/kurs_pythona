#modul do przegladania stron www
from lista5_zad1 import zrob_cos_na_stronie

odwiedzone_strony=set([])


def przegladaj(strona, funkcja, glebokosc, glebokosc_poczatkowa):
    # jesli to pierwsze wywolanie funkcji, to resetuj zbior odwiedzonych stron
    if glebokosc ==glebokosc_poczatkowa:
        odwiedzone_strony = set([])
    if 0 < glebokosc and strona not in odwiedzone_strony:
        odwiedzone_strony.add(strona)
        funkcja(strona)
        przegladaj(strona,funkcja,glebokosc-1,glebokosc_poczatkowa)



    #wykonaj akcje dla strony

    # znajdz wszystkie linki na stronie i wykonaj dla nich ta akcje,
    # jesli licznik<glebokosc

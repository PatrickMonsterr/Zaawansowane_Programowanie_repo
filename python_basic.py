# ==========================================================
# DANE
# ==========================================================
imie1 = "Kuba"
imie2 = "Alek"
imie3 = "Patryk"
imie4 = "Magda"
imie5 = "Jacek"

liczby = [1, 2, 3, 4, 5]
liczby10 = [1,2,3,4,5,6,7,8,9,10]


# ==========================================================
# a) Funkcja otrzymuje imiona w parametrach i wyświetla je
# ==========================================================
def WypiszImiona(imie1, imie2, imie3, imie4, imie5):
    print(imie1, imie2, imie3, imie4, imie5)


# ==========================================================
# b) Funkcja mnoży każdy element listy przez 2 i zwraca wynik
# ==========================================================

# b-i) Wersja z użyciem pętli for
def pomnoz_przez_2for(liczby):
    wynik = []
    for liczba in liczby:
        wynik.append(liczba * 2)
    return wynik

# b-ii) Wersja z użyciem listy składanej
def pomnoz_przez_2lista(liczby):
    return [x * 2 for x in liczby]


# ==========================================================
# c) Funkcja wyświetla tylko parzyste elementy listy
# ==========================================================
def LiczbyParzystenie(liczby10):
    for liczba in liczby10:
        if liczba % 2 == 0:
            print(liczba)


# ==========================================================
# d) Funkcja wyświetla co drugi element listy
# ==========================================================
def wyswietl_co_drugi(liczby):
    for i in range(0, len(liczby), 2):
        print(liczby[i])


# ==========================================================
# WYWOŁANIA
# ==========================================================

# a)
#WypiszImiona(imie1, imie2, imie3, imie4, imie5)

# b-i)
#print(pomnoz_przez_2for(liczby))

# b-ii)
#print(pomnoz_przez_2lista(liczby))

# c)
#print(LiczbyParzystenie(liczby10))

# d)
#print(wyswietl_co_drugi(liczby10))
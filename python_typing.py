# ==========================================================
# FUNKCJE
# ==========================================================

# ==========================================================
# 1) Funkcja przyjmuje 2 stringi (name, surname) i zwraca
#    tekst według wzoru: "Cześć {name} {surname}!"
# ==========================================================
def Funkcja1(name: str, surname: str):
    return (f"Cześć: {name} {surname}")


# ==========================================================
# 2) Funkcja przyjmuje 2 liczby typu int i zwraca ich iloczyn
# ==========================================================
def Funkcja2(x: int, y: int):
    return (x * y)


# ==========================================================
# 3) Funkcja sprawdza, czy liczba jest parzysta
#    i zwraca wynik jako bool (True / False)
# ==========================================================
def Funkcja3(x: int):
    if x % 2 == 0:
        return (True)


# ==========================================================
# 4) Funkcja przyjmuje 3 liczby typu int i sprawdza, czy suma
#    dwóch pierwszych jest większa lub równa trzeciej (bool)
# ==========================================================
def Funkcja4(x: int, y: int, z: int):
    if x + y >= z:
        return (True)
    else:
        return (False)


# ==========================================================
# 5) Funkcja przyjmuje listę i liczbę int, sprawdza czy lista
#    zawiera podaną wartość i zwraca bool
# ==========================================================
def Funkcja5(x: list, y: int):
    for liczba in x:
        if liczba == y:
            return True
    return False


# ==========================================================
# 6) Funkcja przyjmuje 2 listy, łączy je w jedną, usuwa
#    duplikaty, podnosi każdy element do potęgi 3
#    i zwraca nową listę
# ==========================================================
def Funkcja6(list1: list, list2: list) -> list:
    merged = list1 + list2                    # połączenie list
    # usunięcie duplikatów (z zachowaniem kolejności)
    unique = list(dict.fromkeys(merged))
    return [x ** 3 for x in unique]           # podniesienie do potęgi 3


# ==========================================================
# WYWOŁANIA
# ==========================================================

# 1) Wynik zapisany do zmiennej, następnie wyświetlony
wynik = Funkcja1("Patryk", "Budniok")
# print(wynik)

# 2) Wynik zapisany do zmiennej, następnie wyświetlony
wynik2 = Funkcja2(5, 2)
# print(wynik2)

# 3) Wynik zapisany do zmiennej, następnie warunek logiczny
#    wyświetla odpowiedni tekst
wynik3 = Funkcja3(5)

if wynik3:
    print("Liczba Parzysta")
else:
    print("Liczba Nieparzysta")

# 4)
wynik4 = Funkcja4(2, 1, 4)
# print(wynik4)

# 5)
wynik5 = Funkcja5([1, 2, 3, 4, 5], 9)
# print(wynik5)

# 6)
print(Funkcja6([1, 2, 3], [3, 4, 2]))
# [1, 8, 27, 64]

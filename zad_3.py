def is_even(x: int) -> bool:
    return x % 2 == 0


wynik = is_even(5)
if wynik:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

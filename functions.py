import string


def is_palindrome(text: str) -> bool:
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def count_vowels(text: str) -> int:
    vowels = set("aeiouyąęióu")
    return sum(1 for c in text.lower() if c in vowels)


def calculate_discount(price: float, discount: float) -> float:
    if discount < 0 or discount > 1:
        raise ValueError("discount must be between 0 and 1")
    return price * (1 - discount)


def flatten_list(nested_list: list) -> list:
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def word_frequencies(text: str) -> dict:
    cleaned = text.lower()
    for p in string.punctuation:
        cleaned = cleaned.replace(p, " ")
    words = cleaned.split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

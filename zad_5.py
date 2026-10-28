def contains_value(lst: list, value: int) -> bool:
    return value in lst


print(contains_value([1, 2, 3, 4, 5], 3))
print(contains_value([1, 2, 3, 4, 5], 9))

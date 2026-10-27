def merge_cube(list1: list, list2: list) -> list:
    merged = list1 + list2
    unique = list(dict.fromkeys(merged))
    return [x ** 3 for x in unique]

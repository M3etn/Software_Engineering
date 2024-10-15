def remove_element(tup, element):
    if element not in tup:
        return tup
    new_tup = list(tup)
    new_tup.remove(element)
    return tuple(new_tup)
print(remove_element((1, 2, 3), 1))  # (2, 3)


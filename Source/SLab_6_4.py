def get_sliced_tuple(tup, element):
    if element not in tup:
        return ()

    first_index = tup.index(element)
    try:
        last_index = tup.index(element, first_index + 1)
        return tup[first_index:last_index + 1]
    except ValueError:
        return tup[first_index:]
print(get_sliced_tuple((1, 8, 3, 4, 8, 8, 9, 2), 8))
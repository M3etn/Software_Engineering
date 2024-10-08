first = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
second = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
third = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

def modify_grades(grades):
    return [4 if grade == 3 else grade for grade in grades if grade != 2]

print(modify_grades(first))
print(modify_grades(second))
print(modify_grades(third))
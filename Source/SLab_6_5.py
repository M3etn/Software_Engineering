def calc_grades(grades):
    if not grades:
        return 0.0, 0, 0
    avg_grade = sum(grades) / len(grades)
    max_grade = max(grades)
    min_grade = min(grades)
    return avg_grade, max_grade, min_grade
print(calc_grades([90, 85, 92, 88, 95]))
print(calc_grades([]))
print(calc_grades([75, 80, 82, 85, 90, 92, 95]))

def count_digits(digits_str):
    digit_counts = {}
    for digit in digits_str:
        if digit.isdigit():
            digit_int = int(digit)
            if digit_int in digit_counts:
                digit_counts[digit_int] += 1
            else:
                digit_counts[digit_int] = 1
    top_3 = sorted(digit_counts.items(), key=lambda x: x[0])[:3]
    return dict(top_3)
digits_str1 = "1234567890123456"
print(count_digits(digits_str1))


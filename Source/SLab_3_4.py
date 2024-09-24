sentence = input()
print(len(sentence))
lower_sentence = sentence.lower()
print(lower_sentence)
count = 0;
vowels = "aeiou"
for vowel in lower_sentence:
    if vowel in vowels:
        count += 1
print(count)
print(sentence.replace("ugly", "beauty"))
print(sentence.startswith("The"))
print(sentence.endswith("end"))

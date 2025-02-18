# 13. Write a Python program to count the number of characters (characterfrequency) in a string


string = input("Enter a string: ")


char_frequency = {}

for char in string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1


print("Character frequencies:")
for char, freq in char_frequency.items():
    print(f"'{char}': {freq}")

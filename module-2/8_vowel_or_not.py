# Write a Python program to test whether a passed letter is a vowel or not
letter = input("Enter a letter: ").lower()


if letter in 'aeiou':
    print(f"{letter} is a vowel.")
else:
    print(f"{letter} is not a vowel.")

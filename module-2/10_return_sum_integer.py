#Write a Python program that will return true if the  two givenintegervalues are equal or their sum or diference is 5

def check_values(a, b):

    if a == b or a + b == 5 or abs(a - b) == 5:
        return True
    else:
        return False


x = int(input("Enter first integer: "))
y = int(input("Enter second integer: "))


result = check_values(x, y)
print("Result:", result)

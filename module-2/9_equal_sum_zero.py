#Write a Python program to sum of three given integers.  However, if twovalues are equal sum will be zero.
def sum_of_integers(a, b, c):

    if a == b or b == c or a == c:
        return 0
    else:
        return a + b + c


x = int(input("Enter first integer: "))
y = int(input("Enter second integer: "))
z = int(input("Enter third integer: "))


result = sum_of_integers(x, y, z)
print("The result is:", result)

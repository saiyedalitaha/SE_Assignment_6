#Write a Python program to get the Fibonacci series of given range
# Program to generate the Fibonacci series up to a given range


n = int(input("Enter the range: "))

a, b = 0, 1


print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Function to calculate the sum of first n positive integers
def sum_of_integers(n):
    return n * (n + 1) // 2

# Input from user
n = int(input("Enter a positive integer: "))

# Calculate and display the sum
result = sum_of_integers(n)
print("The sum of the first", n, "positive integers is:", result)



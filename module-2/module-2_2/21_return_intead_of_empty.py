#21.Write a Python program to get a string made of the first 2 
#and the last 2chars from a given a string. If the string length 
#is less than 2, return instead of the empty string.
#o Sample String: w3resource' o
#Expected Result: 'w3ce' o 
#SampleString: 'w3' o Expected
#Result:
#'w3w3' o Sample String: ' w' o
#Expected Result: Empty String


def get_first_and_last_two_chars(string):
    if len(string) < 2:
        return "" 
    else:
        return string[:2] + string[-2:]


input_string = input("Enter a string: ")


result = get_first_and_last_two_chars(input_string)
print("Result:", result)


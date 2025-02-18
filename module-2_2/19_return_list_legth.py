#19. Write a Python program to find the first appearance of the 
#substring 'not' and 'poor' from a given string, if 'not' follows the 
#'poor', replace the whole'not'...'poor'substring with 'good'.
#Return the resulting string.
#Write a Python function that takes a list of words and returns 
#the length ofthe longest one.


def replace_not_poor(string):
    
    not_index = string.find('not')
    poor_index = string.find('poor')
    
    
    if not_index != -1 and poor_index != -1 and not_index < poor_index:
      
     string = string[:not_index] + 'good' + string[poor_index + len('poor'):]
    
    return string

def longest_word(words):
    
    return max(len(word) for word in words)



input_string = input("Enter a string: ")
modified_string = replace_not_poor(input_string)
print("Modified string:", modified_string)

words_list = input("Enter a list of words (space-separated): ").split()
longest = longest_word(words_list)
print("Length of the longest word:", longest)


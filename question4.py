'''
Write a function that accepts a list of strings and returns a new list where each string is reversed. 
For example, for the input ["apple", "banana", "cherry"],
 the function should return ["elppa", "ananab", "yrrehc"].
'''
def reversestrings(input_list):
    reversed_list = [s[::-1] for s in input_list] 
    return reversed_list

user_input = input('Enter a list of strings separated by commas: ')
input_list = [s.strip() for s in user_input.split(',')]

result = reversestrings(input_list)
print('The reversed strings are: ',result)

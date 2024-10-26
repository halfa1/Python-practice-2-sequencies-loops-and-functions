'''
Write a function that takes a list of tuples as input, where each tuple contains two elements:
 a string and an integer (e.g., ("apple", 5)).
 The function should return a dictionary where the strings are the keys and the integers are the values.
'''


def dictionaryfromtuples(tuples_list):
    resultant_dictionary ={}
    for key, value in tuples_list:
        resultant_dictionary[key] = value
    return resultant_dictionary

user_input = input('Enter a list of tupples in string integer format comma separated eg (apple:5, :)')
tuples_list = []

for item in user_input.split(','):
    string,integer = item.split(':')
    tuples_list.append((string.strip(),int(integer.strip())))

resultant_dictionary = dictionaryfromtuples(tuples_list)
print('Resultant dictionary: ',resultant_dictionary)
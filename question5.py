'''
Write a Python function that takes a dictionary as input and prints all the keys whose values are even numbers. 
Example: Given the dictionary {'a': 2, 'b': 3, 'c': 4}, the function should print 'a' and 'c'.
'''
def return_even_value_keys(input_dictionary):
    for key,value in input_dictionary.items():
        if value % 2 == 0:
            print(key)

userdata = input('Enter a dictionary eg a:2,b:6,')
input_dictionary = {}

for item in userdata.split(','):
    key, value = item.split(':')
    input_dictionary[key.strip()] = int(value.strip())
print('Keys with even values: ')
return_even_value_keys(input_dictionary)
'''
Write a function that takes a dictionary and an integer n as input and returns a list of keys
 from the dictionary where the value is greater than n. 
For example, for the dictionary {'a': 5, 'b': 12, 'c': 3} and n = 4, the function should return ['a', 'b'].
'''
def keysgreaterthan_n():
    result = []
    dictionary= {}
    user_values = input('Enter a dictionary as key value pairs separated by commas eg a:6,: ')
    n = int(input('Enter a number n compare with:'))

    for item in user_values.split(','):
        key, value = item.split(':')
        dictionary[key.strip()] = int(value.strip())
    for key, value in dictionary.items():
        if value > n:
            result.append(key)
    print(result)

keysgreaterthan_n()
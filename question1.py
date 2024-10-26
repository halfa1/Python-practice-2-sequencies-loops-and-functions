'''
Write a Python program that prints the numbers from 1 to 50 using a for loop.
 For numbers that are divisible by 3, print "Fizz" instead of the number, and 
 for numbers divisible by 5, print "Buzz". For numbers divisible by both, print "FizzBuzz".

'''
for number in range(1,51):
    if number%3 == 0 and number %5 == 0:
        print('FizzBuzz')
    elif number % 5 == 0:
        print('Buzz')
    elif number % 3 == 0:
        print('Fizz')
    else:
        print(number)
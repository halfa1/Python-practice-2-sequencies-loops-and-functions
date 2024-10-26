'''
Given a tuple of numbers, e.g., (10, 20, 30, 40, 50), 
write a Python function using a loop that returns the largest number in the tuple.

'''

numbers = (10,20,30,40,50)
def maximumn():
    largest = numbers[0]
    for i in numbers:
        if i>largest:
            largest=i
    print(f'The largest number from the tuple is: {largest}')

maximumn()
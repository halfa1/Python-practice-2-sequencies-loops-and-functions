'''
Write a Python function that accepts a list of integers and a target sum.
 The function should return True if there are two distinct numbers in the list that add up to the target sum,
  and False otherwise.

'''
def pairs_with_target_sum(numbers,targetSum):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == targetSum:
                return True
        return False


data = input('Enter a list of numbers comma separated: ')
numbers = [int(x.strip()) for x in data.split(',')]
targetSum = int(input('Enter the target sum: '))

result = pairs_with_target_sum(numbers,targetSum)
print('Result: ',result)
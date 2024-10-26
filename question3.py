'''
Given the list nums = [1, 2, 3, 4, 5],
write a Python function using a loop that returns the sum of all the numbers in the list.
'''
def sum():
    nums = [1, 2, 3, 4, 5]
    sum=0
    for i in nums:
     sum=sum+i
    print(sum)
sum()
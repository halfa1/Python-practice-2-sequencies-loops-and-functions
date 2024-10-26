'''
Write a function called remove_duplicates that takes a list as input and returns a new list
 with all duplicate elements removed.
 You cannot use the set function to solve this problem.
'''
def remove_duplicates():
    nonduplicateitems = []
    item_input = input('Enter a list of items separated by comma: ')
    item_input_list = [x.strip() for x in item_input.split(',')]
    #newitem = list(item.split(','))
    for item in item_input_list:
        if item not in nonduplicateitems:
            nonduplicateitems.append(item)

    print("here is the list without duplicates: ")
    print(nonduplicateitems)

remove_duplicates()
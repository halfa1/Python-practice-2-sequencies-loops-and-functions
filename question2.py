'''
Using a while loop, write a function that continuously asks the user for input until they type the word "exit". 
The program should print each word entered by the user before asking for the next input.
'''
def wordcheck():
    while True:
        word = input('Enter a word: ')
        print(f'you entered {word}')
        if word == 'exit':
            print('entered exit')
            break

wordcheck()
from random import randint

""" This program gets 10 numbers from the user and counts
how many of those numbers are greater than 10.
The program also prints all the random numbers selected"""

count = 0
for i in range(10):
    #num = int(input('Enter a number: '))
    num = randint(1, 50)
    if num > 10:
        count=count+1
        print('Random number:',num, 'choosen')
print('There are', count, 'numbers greater than 10.')

# Write a function game() number-guessing game, that takes 2 int parameters defining the range.
#Using some kind of random function to generate random int from the range.
#While user input isn't equal that number, print "Try again!".
#If user guess the number, congratulate him and exit.

def game(intA,intB):
    from random import randint
    randn = randint(int(intA), int(intB))
    guessing_n = input('Input Number from the range: ')
    while int(guessing_n) != randn:
        guessing_n = input('Try again!: ')
    print('Congradulations!!!')

start_range = input('Enter Range Start: ')
end_range = input('Enter Range End: ')
game(start_range,end_range)

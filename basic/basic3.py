#reverse
# Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return the string "gnitset ma I".

def reverse(str):
    index = len(str) - 1
    while index >= 0:
        letter = str[index]
        print(letter, end = '')
        index = index - 1

str1 = input('Enter the string: ')
reverse(str1)

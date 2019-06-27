# Write a function decToBin() that taces decimal integer and outputs its binary representation.
# decToBin Algorithm was used from https://www.geeksforgeeks.org/program-decimal-binary-conversion/
import math

def decToBin(decNumber):
    str_res=""
    p = math.trunc((math.log(decNumber,2)))+1
    # create string with p elemants
    for i in range(p):
        str_res = str_res + " "
    i = 0
    while (decNumber > 0):
        str_res = str_res[:i] +  str(decNumber % 2) + str_res[(i+1):]
        decNumber = int(decNumber / 2)
        i = i + 1
    return str_res

# reverse function from EX3
def reverse(str):
    index = len(str) - 1
    while index >= 0:
        letter = str[index]
        print(letter, end = '')
        index = index - 1

myDecNumber = int(input("Enter decimal number: "))
str_res = decToBin(myDecNumber)
reverse(str_res)

#Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.

input_string = input("Enter a list element separated by space ")
list  = input_string.split()

def sum(list_arg):
    print("Calculating sum of element of input list")
    sum1 = 0
    for num in list_arg:
        sum1 += int (num)
    return(sum1)

def mult(list_arg):
    print("Calculating multiplication of element of input list")
    if  len(list_arg) < 1:
        mult1 = 0
    else:
        mult1 = 1
        for num in list_arg:
            mult1 = mult1 * int (num)
    return(mult1)

try:
    sum_result = sum(list)
    mult_result = mult(list)
    print("Sum:",sum_result)
    print("Multiplitation = ",mult_result)
except:
    print("Enter numeric values")

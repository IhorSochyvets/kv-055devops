#Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
#****
#*********
#******

def histogram(list):
    for x in list:
        z = int(x)
        s1 = "*"*z
        print(s1)

input_string = input("Enter a list element separated by space: ")
list1  = input_string.split()
try:
    histogram(list1)
except:
    print("Enter numeric values")

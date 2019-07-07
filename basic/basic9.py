#Define a function, which takes a string with N opening brackets ("[") and N closing brackets ("]"),
#in some arbitrary order. Determine whether the generated string is balanced; that is,
#whether it consists entirely of pairs of opening/closing brackets (in that order),
#none of which mis-nest. Examples:

#   []        OK   ][        NOT OK
#   [][]      OK   ][][      NOT OK
#   [[][]]    OK   []][[]    NOT OK

# Solution ftom https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/
# was used

open_bracket = ["["]
close_bracket = ["]"]

# Function to check parentheses
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_bracket:
            stack.append(i)
        elif i in close_bracket:
            pos = close_bracket.index(i)
            if ((len(stack) > 0) and
                (open_bracket[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "NOT OK"
    if len(stack) == 0:
        return "OK"

# code
str = input('Enter N opened and N closed brackets in arbitrary order: ')
print(str,"-", check(str))

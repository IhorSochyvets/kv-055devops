#Define a function isPalindrome() that recognizes palindromes (i.e. words that look the same written backwards).
#For example, isPalindrome("radar") should return True.

def is_palindrome(str):
    s1 = ""
    index = len(str) - 1
    while index >= 0:
        s1 = s1 + str[index]
        index = index - 1
    if str == s1:
        s2 = True
    else:
        s2 = False
    print(s2)

str1 = input('Enter a word: ')
str1 = str1.upper()
is_palindrome(str1)

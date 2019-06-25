#Define a function caesarCipher that takes string and key(number), whuch returns encrypted string
# all symbols: ' abcdefghijklmnopqrstuvwxyz'

alpha = ' abcdefghijklmnopqrstuvwxyz'
n = int(input('Enter shift: '))
str = input('Enter phrase: ').strip()

def caesar_cipher(str1):
    res = ''
    for c in str1:
        for i in range(len(alpha)-1):
            if c == alpha[i]:
                res = res + alpha[i+n]
    return(res)

result = caesar_cipher(str)
print('Result: ',result)

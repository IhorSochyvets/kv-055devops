#Define a function caesarCipher that takes string and key(number), whuch returns encrypted string
# all symbols: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# solution was used from http://teachen.info/cspp/unit4/lab04-02.html

def encrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) + key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

#def decrypt(key, message):
#    message = message.upper()
#    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#    result = ""
#
#    for letter in message:
#        if letter in alpha: #if the letter is actually a letter
#            #find the corresponding ciphertext letter in the alphabet
#            letter_index = (alpha.find(letter) - key) % len(alpha)
#
#            result = result + alpha[letter_index]
#        else:
#            result = result + letter
#
#    return result


def main():
    word = input("Enter text to be ciphered: ")
    shift = int(input("Enter the shift: "))

    encrypted = encrypt(shift,word)
    print(encrypted)

#    decrypted = decrypt(shift,encrypted)
#    print(decrypted)

if __name__ == "__main__":
    main()

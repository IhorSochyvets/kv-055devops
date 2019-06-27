# Write a function charFreq() that takes a string and builds a frequency
#listing of the characters contained in it. Represent the frequency listing as
#a Python dictionary. Try it with something like
#charFreq("abbabcbdbabdbdbabababcbcbab").

# Idea was obtained from From https://www.geeksforgeeks.org/counting-the-frequencies-in-a-list-using-dictionary-in-python/

def CountFrequency(str):
    # Creating an empty dictionary
    freq = {}
    for i in range(len(str)):
        if (str[i] in freq):
            freq[str[i]] += 1
        else:
            freq[str[i]] = 1

#    for key, value in freq.items():
#        print ("% d : % d"%(key, value))
    print(freq)

# Driver function

str1 = "abbabcbdbabdbdbabababcbcbab"
CountFrequency(str1)

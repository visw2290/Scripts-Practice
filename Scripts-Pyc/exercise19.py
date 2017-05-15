'''string 17.Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2)'''

def sample(word):
    word1 = word[-2:]
    return word1 * 4


print(sample('python'))
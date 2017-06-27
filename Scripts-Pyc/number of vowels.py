'''Python Program to Count the Number of Each Vowel'''

def VSent(sentence):
    vowels = 'aeiou'
    dict1={}
    for letter in sentence:
        if letter.lower() in vowels:
            dict1.setdefault(letter,0)
            dict1[letter] += 1
    return dict1
print(VSent('Hello, have you tried our turorial section yet?'))

'''Python Program to Sort Words in Alphabetic Order'''

def word_sort(word):
    return ''.join(sorted(' '.join(word).split()))
print(word_sort('hello'))

def sentence_sort(sen):
    sen_list = sen.split()
    sorted_list =[]
    for i in sen_list:
        sorted_list.append(sorted(i))
    return sorted_list
print(sentence_sort('Hey this is viswa for you talking from India'))

def sentence_sort1(sen):
    sen_list = sen.split()
    new_sen = sorted(sen_list)
    for i in new_sen:
        print(i)
sentence_sort1('Hey this is me')
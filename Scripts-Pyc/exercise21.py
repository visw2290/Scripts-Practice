'''dictionary 2.Write a Python script to add a key to a dictionary.'''
dict1 = {'a': 10, 'b':20, 'c':40}

def dict(key,value):
    dict1.setdefault(key,0)
    dict1[key] = value

dict('d',80)
print(dict1)

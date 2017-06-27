'''Given a string, return a string where for every char in the original, there are two chars.

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'''


'''My Program'''

def double_char(str):
  newstr=''
  for letter in str:
    newstr=newstr + letter*2
  return newstr

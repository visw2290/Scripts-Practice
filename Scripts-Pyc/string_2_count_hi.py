'''Return the number of times that the string "hi" appears anywhere in the given string.

count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2'''


'''My Program'''

def count_hi(str):
  count = 0
  for i in range(len(str)):
    chunk = str[i:i+2]
    if chunk == 'hi':
      count += 1
    else:
      continue
  return count
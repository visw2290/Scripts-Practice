'''Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'''

'''My Program'''

def first_half(str):
  half_len=len(str)/2
  return str[0:half_len]
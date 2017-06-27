'''palindrome'''

def pal(word):
    if word.replace(' ','').lower() == word[::-1].replace(' ' ,'').lower():
        return 'String is palindrome'
    else:
        return 'String is not palindrome'
print(pal('nurses run'))

def pal1(word):
    l=len(word)
    for i in word:
        if i == word[l-1]:
            l -= 1
            continue
        else:
            return 'String is not palindrome'
    return 'String is Palindrome'
print(pal1('madam'))

def palnum(number):
    sum = 0
    n = number
    while n!=0:
        rem=n%10
        sum = sum*10+rem
        n = n//10
    if sum == number:
        return 'Number is Palindrome'
    else:
        return 'Number is not Palindrome'
print(palnum(54345))
import datetime
today = datetime.datetime.today() # gives date and time
dateonly = datetime.date.today() # gives only date
text = today.strftime('%d-%m-%y %H:%M:%S.%f') # %f gives milliseconds too
text2 = dateonly.strftime('%B, %d-%y') # %B gives months in words
print(text)
print(text2)

now = datetime.datetime.now() # gives date and time
text1 = '{tod.day}-{tod.month}-{tod.year} {tod.hour}:{tod.minute}:{tod.second} '.format(tod = now)
text3 = now.strftime('%A, %d-%m-%y %H:%M:%S.%f')[:-3]
print('The current time is %s'%(text3))
print(text1)
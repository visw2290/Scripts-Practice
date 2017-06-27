'''The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True'''

'''Program written by me'''

def sleep_in(weekday, vacation):
  if weekday == False and vacation == False:
    return True
  elif weekday == True and vacation == False:
    return False
  elif weekday == False and vacation == True:
    return True
  else:
    return True

'''How this program can be written'''

def sleep_in_1(weekday,vacation):
    if not weekday or vacation:
        return True
    else:
        return False

print(sleep_in_1(True, False))

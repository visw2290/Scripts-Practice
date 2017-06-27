'''Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True'''


'''My Program'''

def array123(nums):
  list_seq = [1,2,3]
  for i in range(len(nums)):
    chunk = nums[i:i+3]
    if chunk == list_seq:
      return True
  return False


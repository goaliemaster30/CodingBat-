# string_times
'''Given a string and a non-negative int n, return a larger
string that is n copies of the original string.'''

def string_times(str, n):
  if n >= 0:
    return str * n
  else:
    return "Wrong"

# front_times
'''Given a string and a non-negative int n, we'll say that the front
of the string is the first 3 chars, or whatever is there if the string
is less than length 3. Return n copies of the front; '''

def front_times(str, n):
  if n >= 0:
    if len(str) < 3:
      return str * n
    else:
      return str[0:3] * n

# string_bits
'''Given a string, return a new string made of every other char starting
with the first, so "Hello" yields "Hlo".'''

def string_bits(str):
  new_word = ""
  for char in range(len(str)):
      if char % 2 == 0:
        new_word += str[char]
  return new_word

# string_splosion
'''Given a non-empty string like "Code" return a string like "CCoCodCode".'''
def string_splosion(str):
  new_word = ""
  for char in range(len(str)):
      new_word = new_word + str[:char+1]
  return new_word

# last2
'''Given a string, return the count of the number of times that a substring
length 2 appears in the string and also as the last 2 chars of the string,
so "hixxxhi" yields 1 (we won't count the end substring).'''

def last2(str):
  count = 0
  if len(str) < 2:
    return count
  last2 = str[-2:]
  for x in range(len(str)-2):
    sub = str[x:x+2]
    if sub == last2:
      count += 1
  return count


# array_count9
'''Given an array of ints, return the number of 9's in the array. '''

def array_count9(nums):
  count = 0
  for x in nums:
    if x == 9:
      count += 1
  return count

# array_front9
'''Given an array of ints, return True if one of the first 4 elements in
the array is a 9. The array length may be less than 4.'''

def array_front9(nums):
  for x in nums[0:4]:
    if x == 9:
      return True
  return False

# array123
'''Given an array of ints, return True if .. 1, 2, 3, .. appears in the array somewhere.'''

def array123(nums):
  for x in range(len(nums)-2):
    if nums[x] == 1 and nums[x+1] == 2 and nums[x+2] == 3:
      return True
  return False

# string_match
'''Given 2 strings, a and b, return the number of the positions where they contain the
same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and
"az" substrings appear in the same place in both strings.'''

def string_match(a, b):
  count = 0
  shorter_string = min(len(a),len(b))
  for x in range(shorter_string-1):
   a_sub = a[x:x+2]
   b_sub = b[x:x+2]
   if a_sub == b_sub:
     count += 1
  return count

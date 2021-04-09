def is_palindrome(string):
  """
  The function takes a word as input, determines whether it is a palindrome and returns a boolean value
  """
  if string == string[::-1]:
    return True
  return False

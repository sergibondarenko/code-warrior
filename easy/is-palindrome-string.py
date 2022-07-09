# Check whether a string is a valid palindrome

# Time O(n), space O(1)
class Solution:
  def __is_palindrome(self, input, i, j):
    while i < j:
      while i < j and not input[i].isalnum():
        i += 1

      while i < j and not input[j].isalnum():
        j -= 1

      if input[i] != input[j]:
        return False
      
      i += 1
      j -= 1
    
    return True


  def is_palindrome(self, input):
    i = 0
    j = len(input) - 1

    while i < j:
      if input[i] != input[j]:
        return self.__is_palindrome(input, i + 1, j) or self.__is_palindrome(input, i, j - 1)
      
      i += 1
      j -= 1

    return True

input = 'anna'
expected = True
output = Solution().is_palindrome(input)
print(output == expected)

input = 'a n?na'
expected = True
output = Solution().is_palindrome(input)
print(output == expected)

input = 'annab'
expected = True
output = Solution().is_palindrome(input)
print(output == expected)

input = 'annabb'
expected = False
output = Solution().is_palindrome(input)
print(output == expected)
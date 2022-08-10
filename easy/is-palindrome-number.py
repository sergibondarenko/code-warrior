# Given a number find if it is a palindrome

class Solution:
  # Time O(1), space O(1)
  def is_palindrome(self, num):
    if num < 0:
      return False
    return int(str(num)[::-1]) == num

  # Time O(1), space O(1)
  def is_palindrome2(self, num):
    if num < 0:
      return False

    rev = 0
    n = num

    while n > 0:
      rev += n % 10
      n //= 10

      if n > 0:
        rev *= 10

    return rev == num

n = 121
expected = True
output = Solution().is_palindrome2(n)
print(output == expected, output, expected)

n = 122
expected = False
output = Solution().is_palindrome2(n)
print(output == expected, output, expected)

n = -121
expected = False
output = Solution().is_palindrome2(n)
print(output == expected, output, expected)
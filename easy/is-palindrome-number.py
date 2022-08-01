# Given a number find if it is a palindrome

# Time O(log10), space O(1)
class Solution:
  def is_palindrome(self, num):
    if (num < 0):
      return False

    n = num
    reversed_n = 0

    while (n != 0):
      reversed_n += n % 10
      n //= 10

      if (n != 0):
        reversed_n *= 10

    return num == reversed_n

n = 121
expected = True
output = Solution().is_palindrome(n)
print(output == expected, output, expected)

n = 122
expected = False
output = Solution().is_palindrome(n)
print(output == expected, output, expected)

n = -121
expected = False
output = Solution().is_palindrome(n)
print(output == expected, output, expected)
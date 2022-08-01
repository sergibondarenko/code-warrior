# Given integer n, return an array where:
# result[i] == 'FizzBuzz' if i is divisible by 3 and by 5
# result[i] == 'Fizz' if i is divisible by 3
# result[i] == 'Buzz' if i is divisible by 5
# result[i] == 'i' if i doesn't satisfy the conditions above

# Time O(n), space O(n)
class Solution:
  def __is_divisible_by(self, n, byN):
    return n % byN == 0
  
  def fizz_buzz(self, n):
    result = []

    for i in range(1, n + 1):
      if self.__is_divisible_by(i, 3) and self.__is_divisible_by(i, 5):
        result.append('FizzBuzz')
      elif self.__is_divisible_by(i, 3):
        result.append('Fizz')
      elif self.__is_divisible_by(i, 5):
        result.append('Buzz')
      else:
        result.append(str(i))

    return result

n = 6
# expected = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz']
output = Solution().fizz_buzz(n)
print(output)
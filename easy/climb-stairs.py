# It takes n steps to reach the top. You can step either 1 or 2 steps.
# How many distinct ways (permutations) you can climb to the top?

# Time O(n), space O(n)
class Solution:
    def __memoKey(self, i, n):
        return str(i) + str(n)
    
    def __climbStairs(self, i, n, memo):
        if i > n:
            return 0
        
        if i == n:
            return 1
        
        key = self.__memoKey(i, n)
        if key in memo:
            return memo[key]
        
        result = self.__climbStairs(i + 1, n, memo) + self.__climbStairs(i + 2, n, memo)
        memo[key] = result
        
        return result

    def __fibonacciNumber(self, n, first = 0):
      second = first + 1

      for _ in range(first, n):
        third = first + second
        first = second
        second = third

      return second
    
    def climbStairs(self, n):
        # memo = {}
        # return self.__climbStairs(0, n, memo)
        return self.__fibonacciNumber(n)

n = 3
output = Solution().climbStairs(n)
# 1 + 1 + 1
# 1 + 2
# 2 + 1
expected = 3
print(output == expected, output, expected)
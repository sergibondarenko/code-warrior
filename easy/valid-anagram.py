# Given to strings s and t return true if t is anagram of s

# Time O(n), space O(1)
class Solution:
    def __counterKey(self, char):
        return ord(char) - ord('a')

    def __isLetter(self, char):
      return ord(char) >= ord('a') and ord(char) <= ord('z')
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counters = [0] * 26
        
        for i in range(len(s)):
          char = s[i].lower()
          if self.__isLetter(char):
            counters[self.__counterKey(char)] += 1
        
        for i in range(len(t)):
          char = t[i].lower()
          if self.__isLetter(char):
            counters[self.__counterKey(char)] -= 1
            
        for counter in counters:
            if counter != 0:
                return False
            
        return True

s = 'silent'
t = 'listen'
expected = True
output = Solution().isAnagram(s, t)
print(output == expected, output, expected)

s = 'cat'
t = 'rat'
expected = False
output = Solution().isAnagram(s, t)
print(output == expected, output, expected)

s = 'a gentleman'
t = 'Elegant man'
expected = True
output = Solution().isAnagram(s, t)
print(output == expected, output, expected)

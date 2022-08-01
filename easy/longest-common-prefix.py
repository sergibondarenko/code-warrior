# Find the longest common prefix sting amongst words in list

# megabyte
# megaton
# meg
# result = meg

# Time O(n), space O(1)
class Solution:
  def longestCommonPrefix(self, list):
    prefix = list[0]

    for i in range(1, len(list)):
      word = list[i]

      while word.find(prefix) != 0:
        prefix = prefix[:-1]

        if len(prefix) == 0:
          return ''

    return prefix

list = ['megabyte', 'megaton', 'meg']
expected = 'meg'
output = Solution().longestCommonPrefix(list)
print(output == expected, output, expected)
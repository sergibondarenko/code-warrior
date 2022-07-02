class Solution:
  def is_valid_parenthesis(self, input):
    stack = []
    map = {
      ')': '(',
      ']': '[',
      '}': '{'
    }

    for ch in input:
      if ch in map:
        if stack.pop() != map[ch]:
          return False
      else:
        stack.append(ch)

    if len(stack) > 0:
      return False

    return True

input = '([{}])()'
expected = True
output = Solution().is_valid_parenthesis(input)
print(output == expected, output)

input = '(]'
expected = False
output = Solution().is_valid_parenthesis(input)
print(output == expected, output)

input = '(('
expected = False
output = Solution().is_valid_parenthesis(input)
print(output == expected, output)
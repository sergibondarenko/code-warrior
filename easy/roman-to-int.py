# Convert roman number to integer

roman_nums = {
  'I': 1,
  'V': 5,
  'X': 10,
  'L': 50,
  'C': 100,
  'D': 500,
  'M': 1000
}

class Solution:
  # Time O(1), space O(1)
  def roman_to_int(self, input):
    result = roman_nums[input[-1]]

    for i in reversed(range(len(input) - 1)):
      curr = roman_nums[input[i]]
      prev = roman_nums[input[i + 1]]

      if curr > prev:
        result += curr
      else:
        result -= curr

    return result 

input = 'MCMLIV'
expected  = 1954
output = Solution().roman_to_int(input)
print(output == expected, output)

# Given a list of numbers, return true if a number appears at least twice

# Time O(n), space O(n)
class Solution:
  def containsDuplicates(self, nums):
    unique_nums = set()

    for n in nums:
      if n in unique_nums:
        return True

      unique_nums.add(n)

    return False

nums = [1,2,3,3]
expected = True
output = Solution().containsDuplicates(nums)
print(output == expected, output, expected)

nums = [1,2,3]
expected = False
output = Solution().containsDuplicates(nums)
print(output == expected, output, expected)
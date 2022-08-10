# Given a list of sorted numbers remove all duplicates in-place.

# Time O(n), space O(1)
class Solution:
  def removeDuplicates(self, nums):
    i = 0

    for j in range(1, len(nums)):
      if nums[i] != nums[j]:
        i += 1
        nums[i] = nums[j]

    return i + 1

list = [0, 0, 1, 1, 1, 2]
expected = 3
output = Solution().removeDuplicates(list)
print(output == expected, output)
# Given nums = [1, 15, 5, 8] and target = 13 find any two numbers in nums, which sum is equal to target 

class Solution:
  # Time O(n), space O(n)
  def twoSum(self, nums, target):
    hashmap = {}

    for i in range(len(nums)):
      x = target - nums[i]

      if x in hashmap:
        return [x, nums[i]]

      hashmap[nums[i]] = i

nums = [1, 15, 5, 8]
target = 13
# 5, 8
print(Solution().twoSum(nums, target))
# Given a list of integers sorted in the ascending order, find if integer x is in the list

# Time O(logn), space O(1)
class Solution:
  def search(self, nums, x):
    i = 0
    j = len(nums) - 1

    while i <= j:
      mid = (i + j) // 2

      if nums[mid] == x:
        return mid
      elif nums[mid] < x:
        i = mid + 1
      else:
        j = mid - 1

    return -1

nums = [-2, -1, 0, 3, 6, 7, 9, 10]
x = 7
expected = 5
output = Solution().search(nums, x)
print(output == expected, output, expected)

nums = [-2, -1, 0, 3, 6, 7, 9, 10]
x = -2
expected = 0
output = Solution().search(nums, x)
print(output == expected, output, expected)

nums = [-2, -1, 0, 3, 6, 7, 9, 10]
x = 5
expected = -1
output = Solution().search(nums, x)
print(output == expected, output, expected)

nums = [-1,0,3,5,9,12]
x = 13
expected = -1
output = Solution().search(nums, x)
print(output == expected, output, expected)
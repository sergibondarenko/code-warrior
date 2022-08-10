# Given array of size n return a majority element.
# The majority elelemnt is present more then n / 2 times.

class Solution:
    # Time O(n), space O(n)
    def majorityElement(self, nums):
        freqs = {}
        maxFreq = float('-inf')
        result = -1
        
        for n in nums:
            if n in freqs:
                freqs[n] += 1
            else:
                freqs[n] = 1
                
            if freqs[n] > maxFreq:
                result = n
                maxFreq = freqs[n]

        return result
        
nums = [3, 1, 2, 3, 2, 3]
expected = 3
output = Solution().majorityElement(nums)
print(output == expected, output, expected)        
      
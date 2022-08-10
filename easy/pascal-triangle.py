# Given n rows create Pascal triangle

#    1
#   1 1
#  1 2 1
# 1 3 3 1

# (n k) = (n - 1, k - 1) + (n - 1, k)


class Solution:
  # Time O(n^2), space O(n)
  def generateTriangle(self, nrows):
    result = []

    for nrow in range(nrows):
      row = [None for i in range(nrow + 1)]
      row[0] = 1
      row[-1] = 1

      for i in range(1, len(row) - 1):
        row[i] = result[nrow - 1][i - 1] + result[nrow - 1][i]
      
      result.append(row)

    return result

nrows = 7
# [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1]]
print(Solution().generateTriangle(nrows))

nrows = 1
# [[1]]
print(Solution().generateTriangle(nrows))
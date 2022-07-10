# You can select one day to purchase and one day to sell.
# Calculate max profit you can achieve from buying and selling stocks.

from cmath import inf

# Time O(n), space O(1)
class Solution:
  def max_profit(self, prices):
    min_price = inf
    max_profit = 0

    for i in range(len(prices)):
      price = prices[i]

      if price < min_price:
        min_price = price

      curr_max_profit = price - min_price

      if curr_max_profit > max_profit:
        max_profit = curr_max_profit

    return max_profit

prices = [2,1,3,7,10,2]
expected = 9
output = Solution().max_profit(prices)
print(output == expected)
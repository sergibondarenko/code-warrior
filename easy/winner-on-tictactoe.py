# Given a number of moves where move[i] is [row, column], find a winner in the tictactoe game.
# Player A always moves first.

# Time O(n), space O(n)
class Solution:
  def __isDiagonal(self, row, col):
    return row == col

  def __isAntiDiagonal(self, row, col, n):
    return row + col == n - 1
  
  def tictactoe(self, moves, n = 3):
    rows = [0] * n
    cols = [0] * n
    diag = 0
    antiDiag = 0
    player = 1

    for r, c in moves:
      rows[r] += player
      cols[c] += player

      if self.__isDiagonal(r, c):
        diag += player

      if self.__isAntiDiagonal(r, c, n):
        antiDiag += player

      for val in (rows[r], cols[c], diag, antiDiag):
        if val == n:
          return 'A'
        elif val == n * -1:
          return 'B'

      player *= -1

    if len(moves) != n * n:
      return 'Pending'
    
    return 'Draw'


moves = [[0,0],[2,0],[1,1],[2,1],[1,2],[2,2]]
expected = 'B'
output = Solution().tictactoe(moves)
print(output == expected, output, expected)

moves = [[0,0],[2,0],[1,1],[2,1],[1,2]]
expected = 'Pending'
output = Solution().tictactoe(moves)
print(output == expected, output, expected)
# Given a stream of integers calculate average in window size n

from collections import deque

class Average:
  def __init__(self, size):
    self.size = size
    self.queue = deque()
    self.sum = 0

  def next(self, n):
    self.queue.append(n)
    tail = self.queue.popleft() if len(self.queue) > self.size else 0
    self.sum += -tail + n
    return self.sum / min(self.size, len(self.queue))

# size = 3
solution = Average(3) 

output = solution.next(5) # 5 / 1 == 5
print(output == 5, output, 5)

output = solution.next(7)
print(output == 6, output, 6) # (5 + 7) / 2 == 6

output = solution.next(9)
print(output == 7, output, 7) # (5 + 7 + 9) / 3 == 7

output = solution.next(15)
print(output == 10.333333333333334, output, 10.333333333333334) # (7 + 9 + 15) / 3 == 10.333333333333334 
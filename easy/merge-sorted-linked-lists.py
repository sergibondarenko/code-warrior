# Merge two sorted linked lists

# List1: 1 -> 2
# List2: 0 -> 3
# Result: 0 -> 1 -> 2 -> 3

class Node:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

  def __repr__(self):
    res = str(self.val)
    if self.next:
      res += str(self.next)
    return res

# Time O(n), space O(1)
class Solution:
  def mergeLists(self, l1, l2):
    sentinel = Node(-1)
    curr = sentinel

    while l1 and l2:
      if l1.val < l2.val:
        curr.next = l1
        l1 = l1.next
      else:
        curr.next = l2
        l2 = l2.next

      curr = curr.next

    curr.next = l1 if l1 else l2

    return sentinel.next

l1 = Node(1, Node(2))
l2 = Node(0, Node(3))
print(Solution().mergeLists(l1, l2)) # 0123
# Reverse linked list

# 1 -> 2 -> 3
# becomes
# 3 -> 2 -> 1 

class Node:
  def __init__(self, val, next = None) -> None:
    self.val = val
    self.next = next

  def __repr__(self) -> str:
    res = str(self.val)
    if self.next:
      res += str(self.next)
    return res

# Time O(n), space O(1)
class Solution:
  def reverse_linked_list(self, head):
    curr = head
    prev = None

    while curr:
      tmp = curr.next
      curr.next = prev
      prev = curr
      curr = tmp

    return prev

head = Node(1, Node(2, Node(3)))
print(Solution().reverse_linked_list(head)) # 321
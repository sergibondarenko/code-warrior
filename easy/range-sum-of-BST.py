# Given two integers low and high return the sum of values of all nodes where
# low <= node value <= high

class Node:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

# BFS
# Time O(n), space O(n)
class Solution:
    def rangeSumBST(self, root, low, high):
        def isInRange(val):
            return low <= val <= high

        result = 0
        queue = [root]
        
        while len(queue) > 0:
            _queue = []
            
            for node in queue:
                if isInRange(node.val):
                    result += node.val
                    
                if node.left and isInRange(node.left.val):
                    _queue.append(node.left)
                    
                if node.right and isInRange(node.right.val):
                    _queue.append(node.right)
                    
                queue = _queue
        
        return result

#      15
#     /  \
#    6   23
#   / \    \  
#  4   7    71
#   \       /        
#    5     50 

root = Node(15, Node(6, Node(4, None, Node(5)), Node(7)), Node(23, None, Node(71, Node(50))))
low = 6
high = 30
expected = 51 # 15 + 6 + 7 + 23 = 51
output = Solution().rangeSumBST(root, low, high)
print(output == expected, output, expected) # 6 + 7 +
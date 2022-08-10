# You need to load a truck with boxes
# You are given the truck size, which represents a number of boxes you can put.
# Also, you got a list of boxes where boxes[i] = [num of boxes, units per box]
# Find maximum number of units you can put on the truck. 

class Solution:
  # Time O(nlogn), space O(1)
  def max_units(self, boxes, truck_size):
    boxes.sort(key = lambda x: x[1], reverse=True) 
    
    i = 0
    units = 0

    while truck_size > 0 and i < len(boxes):
      boxes_taken = min(boxes[i][0], truck_size)
      units += boxes_taken * boxes[i][1]
      i += 1
      truck_size -= boxes_taken

    return units

boxes = [[2,3],[1,2],[10,1]]
truck_size = 4
expected = 9
output = Solution().max_units(boxes, truck_size)
print(output == expected, output, expected)


import time


class Node():
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right



def valuesAtHeight(root, height):
    height -= 1

    if(root.left is not None):
        valuesAtHeight(root.left, height)

    if(root.right is not None):
        valuesAtHeight(root.right, height)

    if(height == 0):
        print(root.value)

    
#     1
#    / \
#   2   3
#  / \   \
# 4   5   7

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)

start = time.time()
valuesAtHeight(a, 3)
end = time.time()
print( "time : ", end - start)


def valuesAtHeight(node, depth):
  if not node:
    return []

  if depth == 1:
    return [node.value]

  return valuesAtHeight(node.left, depth - 1) + valuesAtHeight(node.right, depth - 1)
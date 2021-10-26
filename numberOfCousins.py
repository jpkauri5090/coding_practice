class Node(object):
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

class Solution(object):
    def __get_hash_map_of_tree(self, root, val, depth, hashMap):
        depth += 1

        hashMap[root.value] = depth

        if root.left is not None:
            self.__get_hash_map_of_tree(root.left, val, depth, hashMap)

        if root.right is not None:
            self.__get_hash_map_of_tree(root.right, val, depth, hashMap)

        return hashMap

    def list_cousins(self, root, val):

        initDepth = 0
        initHash = {0:-1}
        finalHash = self.__get_hash_map_of_tree(root, val, initDepth, initHash)
        targetKey = finalHash[val]

        results = [key for key, value in finalHash.items() if value == targetKey and key is not val]

        return results



root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(6)
root.right = Node(3)
root.right.right = Node(5)

print Solution().list_cousins(root, 6)


# class Solution(object):
#   def _nodes_at_height(self, node, height, exclude):
#     if node == None or node == exclude:
#       return []
#     if height == 0:
#       return [node.value]
#     return (self._nodes_at_height(node.left, height - 1, exclude) +
#             self._nodes_at_height(node.right, height - 1, exclude))

#   def _find_node(self, node, target, parent, height):
#     if not node:
#       return False
#     if node == target:
#       return (height, parent)
#     return (self._find_node(node.left, target, node, height + 1) or
#             self._find_node(node.right, target, node, height + 1))

#   def list_cousins(self, node, target):
#     height, parent = self._find_node(node, target, None, 0)
#     return self._nodes_at_height(node, height, parent)
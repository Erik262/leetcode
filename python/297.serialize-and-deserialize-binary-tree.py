from typing import Optional
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        coded = []
        def dfs(node: Optional[TreeNode]):
            if not node:
                coded.append("None")
                return
            
            coded.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ";".join(coded)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.index = 0
        decoded = str(data).split(";")
        def dfs():
            if self.index >= len(decoded):
                return None
            
            val = decoded[self.index]
            self.index += 1

            if val == "None":
                return None

            tree = TreeNode(int(val))
            tree.left = dfs()
            tree.right = dfs()
            
            return tree

        return dfs()

  
def list_to_tree(data: list[Optional[int]]) -> Optional[TreeNode]:
    if not data:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in data]
    kid_index = 1
    for node in nodes:
        if node is not None:
            if kid_index < len(nodes):
                node.left = nodes[kid_index]
                kid_index += 1
            if kid_index < len(nodes):
                node.right = nodes[kid_index]
                kid_index += 1
    return nodes[0]


def tree_to_list(root: Optional[TreeNode]) -> list[Optional[int]]:
    if root is None:
        return []
    result: list[Optional[int]] = []
    queue: list[Optional[TreeNode]] = [root]
    while queue:
        node = queue.pop(0)
        if node is not None:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

# Your Codec object will be instantiated and called as such:
root = [1,2,3,None,None,4,5]

ser = Codec()
deser = Codec()

serialized = ser.serialize(list_to_tree(root))
# print(serialized)

ans = deser.deserialize(serialized)

print(tree_to_list(ans))
# @lc code=end


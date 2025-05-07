from typing import Optional
from collections import deque
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        def count_node(root: TreeNode, root_val):
            if not root:
                return 0
            
            result = 0
            
            if root.val >= root_val:
                result += 1

            maxVal = max(root.val, root_val)

            result += count_node(root.left, maxVal)
            result += count_node(root.right, maxVal)

            return result

        return count_node(root, root.val)

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


root = [3,1,4,3,None,1,5] # 4
# root = [3,3,None,4,2] # 3
# root = [1] # 1

print(Solution().goodNodes(list_to_tree(root)))
        
# @lc code=end


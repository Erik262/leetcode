from typing import Optional
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.max_diam = 0
        self.depth(root)

        return self.max_diam

    def depth(self, root: Optional[TreeNode]):
        if not root:
            return 0
        
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        self.max_diam = max(self.max_diam, left_depth + right_depth)
        
        return 1 + max(left_depth, right_depth)

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



root = [1,2,3,4,5] # 3
# root = [1,2] # 1
# root = [1,None,2,3,4,5] # 3

print(Solution().diameterOfBinaryTree(list_to_tree(root)))


        
# @lc code=end


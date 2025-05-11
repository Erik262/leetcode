from typing import Optional
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.summe = float("-inf")
        
        def sumit(root: Optional[TreeNode]):
            if not root:
                return 0
            
            left_tree = max(0, sumit(root.left))
            right_tree = max(0, sumit(root.right))

            self.summe = max(self.summe, root.val + left_tree + right_tree)

            return root.val + max(left_tree, right_tree)
        
        sumit(root)
        return self.summe

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
        
root = [1,2,3] # 6
# root = [-10,9,20,None,None,15,7] # 42

print(Solution().maxPathSum(list_to_tree(root)))

# @lc code=end
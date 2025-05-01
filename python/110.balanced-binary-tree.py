from typing import Optional
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _, balanced = self.depth(root)

        return balanced

    def depth(self, root: Optional[TreeNode]):
        balanced = True
        if not root:
            return (0, balanced)
        
        left_depth, left_bal = self.depth(root.left)
        right_depth, right_bal = self.depth(root.right)

        balanced = left_bal and right_bal and abs(left_depth - right_depth) <= 1
        
        return (1 + max(left_depth, right_depth), balanced)

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


root = [1,2,3,None,None,4] # True
# root = [1,2,3,None,None,4,None,5] # False
# root = [] # True
print(Solution().isBalanced(list_to_tree(root)))
        
# @lc code=end


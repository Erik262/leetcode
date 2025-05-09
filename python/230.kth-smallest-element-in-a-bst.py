from typing import Optional
from collections import deque
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k

        def kthSearch(root: Optional[TreeNode]):
            if not root:
                return None
            
            val = kthSearch(root.left)
            if val is not None:
                return val

            self.count -= 1
            if self.count == 0:
                return root.val
            
            val = kthSearch(root.right)
            if val is not None:
                return val
            

        return kthSearch(root)


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


root = [3,1,4,None,2] # 1
k = 1

root = [5,3,6,2,4,None,None,1] # 3
k = 3


print(Solution().kthSmallest(list_to_tree(root), k))
# @lc code=end
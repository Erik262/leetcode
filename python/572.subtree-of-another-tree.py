from typing import Optional
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = self.subTree(root, subRoot)
        
        return res
    
    def subTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]):
        if not root:
            return False
        if not subRoot:
            return True

        if root.val == subRoot.val:
            if self.compare(root, subRoot):
                return True
        
        left = self.subTree(root.left, subRoot)
        right = self.subTree(root.right, subRoot)

        return left or right

    def compare(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if not p and not q:
            return True
        elif not p and q:
            return False
        elif p and not q:
            return False
        elif p.val != q.val:
            return False
        else:
            left_node = self.compare(p.left, q.left)
            right_node = self.compare(p.right, q.right)

            return left_node and right_node

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


root = [3,4,5,1,2] # True
subRoot = [4,1,2]

root=[1,1] # True
subRoot=[1]

# root = [1,2,3,4,5] # True
# subRoot = [2,4,5]

# root = [1,2,3,4,5,None,None,6] # False
# subRoot = [2,4,5]

print(Solution().isSubtree(list_to_tree(root),list_to_tree(subRoot)))

# @lc code=end


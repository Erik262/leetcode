from typing import Optional
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p

        while root:
            if p.val > root.val:
                root = root.right
            elif q.val < root.val:
                root = root.left
            else:
                return root

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


root = [5,3,8,1,4,7,9,None,2] # 5
p = 3
q = 8

# root = [6,2,8,0,4,7,9,None,None,3,5] # 6
# p = 2
# q = 8

# root = [6,2,8,0,4,7,9,None,None,3,5] # 2
# p = 2
# q = 4

# root = [2,1] # 2
# p = 2
# q = 1

res = Solution().lowestCommonAncestor(list_to_tree(root),TreeNode(p),TreeNode(q))
print(res.val)

# @lc code=end


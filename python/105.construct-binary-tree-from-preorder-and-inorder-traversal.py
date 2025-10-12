from typing import List, Optional
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_pos = 0
        val_to_index = {val: idx for idx, val in enumerate(inorder)}

        def dfs(l, r):
            if l == r:
                return None
            
            root = preorder[self.pre_pos]
            self.pre_pos += 1

            node = TreeNode(root)
            mid = val_to_index[root]

            node.left = dfs(l, mid)
            node.right = dfs(mid + 1, r)

            return node
        
        return dfs(0, len(inorder))



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
        

preorder = [3,9,20,15,7] # [3,9,20,null,null,15,7]
inorder = [9,3,15,20,7]

# preorder = [-1] # [-1]
# inorder = [-1]

res = Solution().buildTree(preorder, inorder)
print(tree_to_list(res))

# @lc code=end


from typing import List
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
class TreeNode:
    def __init__(self):
        self.child = {}
        self.end = False

    def add_word(self, word: str):

        for c in word:
            if c not in self.child:
                self.child[c] = TreeNode()

            self = self.child[c]
        self.end = True

# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res, visit = set(), set()
        rows, cols = len(board), len(board[0])

        root = TreeNode()
        for word in words:
            root.add_word(word)

        def dfs(i: int, j: int, node: TreeNode, word: str):            
            # boundaries
            if (i < 0 or i >= rows or j < 0 or j >= cols or (i, j) in visit or board[i][j] not in node.child):
                return
            
            visit.add((i, j))
            node = node.child[board[i][j]]
            word += board[i][j]

            if node.end:
                res.add(word)

            dfs(i + 1, j, node, word) # down
            dfs(i - 1, j, node, word) # up
            dfs(i, j + 1, node, word) # right
            dfs(i, j - 1, node, word) # left

            visit.remove((i, j))

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root, "")

        return list(res)
    
        



board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
]
words = ["bat","cat","back","backend","stack"]
# Output: ["cat","back","backend"]


print(Solution().findWords(board, words))

# @lc code=end


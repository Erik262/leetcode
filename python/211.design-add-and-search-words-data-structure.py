#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

class TreeNode:
    def __init__(self):
        self.child = {}
        self.end = False

# @lc code=start
class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.child:
                curr.child[c] = TreeNode()

            curr = curr.child[c]

        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root

        def dfs(node: TreeNode, i: int):
            if i == len(word):
                return node.end
            
            c = word[i]

            if c == '.':
                for child in node.child.values():
                    if dfs(child, i + 1):
                        return True
                return False
            
            else:
                if c not in node.child:
                    return False
                
                return dfs(node.child[c], i + 1)
        
        # print(dfs(curr, 0))
        return dfs(curr, 0)

wd = WordDictionary()
wd.addWord("day")
wd.addWord("bay")
wd.addWord("may")
wd.search("say") # return false
wd.search("day") # return true
wd.search(".ay") # return true
wd.search("b..") # return true


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end


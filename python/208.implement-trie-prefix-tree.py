#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

class TreeNode:
    def __init__(self) -> None:
        self.child = {}
        self.end = False

# @lc code=start
class Trie:

    def __init__(self):
        self.root = TreeNode()


    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.child:
                curr.child[c] = TreeNode()
            
            curr = curr.child[c]
        curr.end = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.child:
                return False
            
            curr = curr.child[c]

        if not curr.end:
            return False

        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.child:
                return False
            curr = curr.child[c]

        return True



prefixTree = Trie()
prefixTree.insert("dog")
prefixTree.search("dog")    # return true
prefixTree.search("do")     # return false
prefixTree.startsWith("do") # return true
prefixTree.insert("do")
prefixTree.search("do")     # return true


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end


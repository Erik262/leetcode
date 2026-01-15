#
# @lc app=leetcode id=1897 lang=python3
#
# [1897] Redistribute Characters to Make All Strings Equal
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        coll = [0] * 26

        for w in words:
            for ch in w:
                coll[ord(ch) - 97] += 1

        for v in coll:
            if v % len(words) != 0:
                return False

        return True
    

words = ["abc","aabc","bc"]

print(Solution().makeEqual(words))
        
# @lc code=end


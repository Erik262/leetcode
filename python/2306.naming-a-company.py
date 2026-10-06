#
# @lc app=leetcode id=2306 lang=python3
#
# [2306] Naming a Company
#
from typing import List

# @lc code=start
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        groups = [set() for _ in range(26)]
        
        for w in ideas:
            groups[ord(w[0]) - 97].add(w[1:])
        
        res = 0
        for i in range(26):
            for j in range(i + 1, 26):
                common = len(groups[i] & groups[j])
                res += 2 * (len(groups[i]) - common) * (len(groups[j]) - common)
        
        return res



ideas = ["coffee","donuts","time","toffee"] # 6
print(Solution().distinctNames(ideas))
# @lc code=end


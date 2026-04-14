#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#
from typing import Counter
# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        buckets = [[] for _ in range(len(s) + 1)]

        for ch, freq in cnt.items():
            buckets[freq].append(ch)

        res = []
        for freq in range(len(s), 0, -1):
            for ch in buckets[freq]:
                res.append(ch * freq)

        return "".join(res)        
# @lc code=end


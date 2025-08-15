from typing import List
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # get last index of character
        last = {}
        for idx, c in enumerate(s):
            last[c] = idx

        start = 0
        end = 0
        result = []

        for idx, c in enumerate(s):
            end = max(end, last[c])

            if idx == end:
                result.append(end - start + 1)
                start = idx + 1

        return result


s = "xyxxyzbzbbisl" # [5, 5, 1, 1, 1]
# s = "abcabc" # [6]

print(Solution().partitionLabels(s))
        
# @lc code=end


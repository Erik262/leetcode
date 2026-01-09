#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#
from typing import Counter
# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt_balloon = Counter("balloon")
        cnt_text = Counter(text)

        result = float("inf")

        for c in cnt_balloon:
            result = min(result, cnt_text[c] // cnt_balloon[c])

        return result


text = "nlaebolko" # 1
text = "loonbalxballpoon" # 2

print(Solution().maxNumberOfBalloons(text))
        
# @lc code=end


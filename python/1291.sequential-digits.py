#
# @lc app=leetcode id=1291 lang=python3
#
# [1291] Sequential Digits
#
from typing import List
# @lc code=start
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        digit = "123456789"

        for length in range(len(str(low)), len(str(high)) + 1):
            for i in range(len(digit) - length + 1):
                num = int(digit[i:i+length])

                if low <= num <= high:
                    res.append(num)

        return res 
# @lc code=end


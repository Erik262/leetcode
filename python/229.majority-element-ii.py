#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        res = []

        for k in cnt:
            if cnt[k] > (len(nums) // 3):
                res.append(k)

        return res
        
# @lc code=end


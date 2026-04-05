#
# @lc app=leetcode id=2483 lang=python3
#
# [2483] Minimum Penalty for a Shop
#

# @lc code=start
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count("Y")
        best_penalty = penalty
        best_hour = 0

        for i, ch in enumerate(customers):
            if ch == "Ys":
                penalty -= 1
            else:
                penalty += 1

            if penalty < best_penalty:
                best_penalty = penalty
                best_hour = i + 1

        return best_hour
    
customers = "YYNY" # 2
# customers = "YYYY" # 2
print(Solution().bestClosingTime(customers))
# @lc code=end


#
# @lc app=leetcode id=1700 lang=python3
#
# [1700] Number of Students Unable to Eat Lunch
#
from typing import List
# @lc code=start
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = Counter(students)

        for sw in sandwiches:
            if cnt[sw] == 0:
                return cnt[0] + cnt[1]
            cnt[sw] -= 1

        return 0


students = [1,1,0,0]
sandwiches = [0,1,0,1] # 0

# students = [1,1,1,0,0,1]
# sandwiches = [1,0,0,0,1,1] # 3


print(Solution().countStudents(students, sandwiches))
        
# @lc code=end


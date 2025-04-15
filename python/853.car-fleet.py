#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, speed in cars:
            time = (target - pos) / speed
            if not stack:
                stack.append(time)

            if stack[-1] < time:
                stack.append(time)

        return len(stack)

target = 10 # 3
position =  [4,1,0,7]
speed =     [2,2,1,1]

# target = 12 # 3
# position =  [10,8,0,5,3]
# speed =     [2 ,4,1,1,3]


# target = 100 # 1
# position =  [0,2,4]
# speed =     [4,2,1]

print(Solution().carFleet(target, position, speed))
        
# @lc code=end


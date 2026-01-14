#
# @lc app=leetcode id=1496 lang=python3
#
# [1496] Path Crossing
#

# @lc code=start
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0,0)}
        curr_pos = [0,0]

        for p in path:
            match p:
                case "N":
                    curr_pos[1] += 1
                case "S":
                    curr_pos[1] -= 1
                case "E":
                    curr_pos[0] += 1
                case "W":
                    curr_pos[0] -= 1

            pos = (curr_pos[0], curr_pos[1])
            if pos in visited:
                return True

            visited.add(pos)

        return False

        
# @lc code=end


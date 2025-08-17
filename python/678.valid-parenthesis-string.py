#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:

        hmap = [0,0]
        for ch in s:
            match ch:
                case '(':
                    hmap[0] = hmap[0] + 1
                    hmap[1] = hmap[1] + 1

                case ')':
                    hmap[0] = hmap[0] - 1
                    hmap[1] = hmap[1] - 1

                case '*':
                    hmap[0] = hmap[0] - 1
                    hmap[1] = hmap[1] + 1

            if hmap[0] < 0: hmap[0] = 0
            if hmap[1] < 0: return False
            
        if hmap[0] == 0:
            return True
        else:
            return False


s = "((**)" # True
s = "(((*)" # False
s = "()" # True
s ="(((((()*)(*)*))())())(()())())))((**)))))(()())()" # False
s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())" # False

print(Solution().checkValidString(s))
        
# @lc code=end


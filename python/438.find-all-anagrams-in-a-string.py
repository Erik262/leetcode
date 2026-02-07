#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
from typing import List
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_freq = [0] * 26
        win_freq = [0] * 26
        result = []

        for c in p:
            p_freq[ord(c) - 97] += 1

        left = 0
        for right in range(len(s)):
            win_freq[ord(s[right]) - 97] += 1

            if right - left + 1 > len(p):
                win_freq[ord(s[left]) - 97] -= 1
                left += 1

            if win_freq == p_freq:
                result.append(left)
        
        return result
    
s = "cbaebabacd"
p = "abc" # [0,6]

s = "abab"
p = "ab" # [0,1,2]
print(Solution().findAnagrams(s, p))
        
# @lc code=end


#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        base_mag = [0] * 26
        need = [0] * 26

        for ch in magazine:
            base_mag[ord(ch) - 97] += 1

        for ch in ransomNote:
            i = ord(ch) - 97
            need[i] += 1

            if need[i] > base_mag[i]:
                return False

        return True
        
# @lc code=end


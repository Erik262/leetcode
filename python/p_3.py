class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hmap = {}
        l = 0
        best = 0

        for r in range(len(s)):
            if s[r] in hmap and hmap[s[r]] >= l:
                l = hmap[s[r]] + 1
            
            tmp_best = r - l + 1
            best = max(tmp_best, best)

            hmap[s[r]] = r

        return best

        
s = "zxyzxyz" # 3
# s = "xxxx" # 1
# s = "abba" # 2
# s = "abcabcbb" # 3
# s = "bbbbb" # 1
# s = "pwwkew" # 3
print(Solution().lengthOfLongestSubstring(s))
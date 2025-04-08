class Solution(object):
    def lengthOfLongestSubstring(self, s):
        c_set = set()
        wl = 0
        l = 0

        for r in range(len(s)):
            while s[r] in c_set:
                c_set.remove(s[l])
                l += 1
            c_set.add(s[r])
            wl = max(wl, len(c_set))

        return wl

        
s = "zxyzxyz" # 3
# s = "xxxx" # 1
# s = "abba" # 2
# s = "abcabcbb" # 3
# s = "bbbbb" # 1
# s = "pwwkew" # 3
print(Solution().lengthOfLongestSubstring(s))
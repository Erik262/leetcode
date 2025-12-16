class Solution(object):
    def isAnagram(self, s, t):
        s_sorted = sorted(s)
        t_sorted = sorted(t)

        return s_sorted == t_sorted
        

s = "anagram"
t = "nagaram"

print(Solution().isAnagram(s,t))
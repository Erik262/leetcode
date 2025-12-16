from collections import defaultdict, Counter

class Solution:
    def minWindow(self, s, t):
        need = Counter(t)
        have = defaultdict(int)
        required = len(need)
        formed = 0
        l = 0
        best_len = float('inf')
        best = (-1, -1)

        for r, ch in enumerate(s):
            if ch in need:
                have[ch] += 1

                if have[ch] == need[ch]:
                    formed += 1

            while required == formed:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best = (l, r)

                if s[l] in need:
                    have[s[l]] -= 1

                    if have[s[l]] < need[s[l]]:
                        formed -= 1

                l += 1

        if best[0] == -1:
            return ""
        
        return s[best[0]:best[1] + 1]

s = "ADOBECODEBANC" # "BABC"
t = "ABC"

# s = "a" # "a"
# t = "a"

# s = "a" # ""
# t = "aa"

# s="OUZODYXAZV" # "YXAZ"
# t="XYZ"

print(Solution().minWindow(s,t))
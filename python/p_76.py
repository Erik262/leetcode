class Solution:
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""
        
        if t == "":
            return ""
        
        t_map = {}
        slid_window = {}

        for c in t:
            t_map[c] = t_map.get(c, 0) + 1

        have = 0 
        need = len(t_map)
        result = [-1, -1]
        result_len = float("infinity")

        l = 0

        for r in range(len(s)):
            c = s[r]
            slid_window[c] = slid_window.get(c, 0) + 1

            if c in t_map and slid_window[c] == t_map[c]:
                have += 1

            while have == need:
                if (r - l + 1) < result_len:
                    result_len = (r - l + 1)
                    result = [l,r]
                slid_window[s[l]] -= 1

                if s[l] in t_map and slid_window[s[l]] < t_map[s[l]]:
                    have -= 1

                l += 1

        if result_len != float("infinity"):
            return s[result[0]: result[1] + 1]
        else:
            return ""

s = "ADOBECODEBANC" # "BABC"
t = "ABC"

# s = "a" # "a"
# t = "a"

# s = "a" # ""
# t = "aa"

# s="OUZODYXAZV" # "YXAZ"
# t="XYZ"

print(Solution().minWindow(s,t))
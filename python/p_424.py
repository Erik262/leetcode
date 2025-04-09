class Solution(object):
    def characterReplacement(self, s, k):
        h_map = {}
        result = 0
        l = 0

        for r in range(len(s)):
            h_map[s[r]] = h_map.get(s[r], 0) + 1

            while ((r - l + 1) - max(h_map.values())) > k:
                h_map[s[l]] -= 1
                l += 1

            result = max(result, (r - l + 1))

        return result


s = "AABABBA"
k = 1 # 4
# s = "ABAB" 
# k = 2 # 4
# s = "XYYX" 
# k = 2 # 4
# s = "AAABABB"
# k = 1 # 5

print(Solution().characterReplacement(s,k))  
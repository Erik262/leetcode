from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        l = 0
        freq_map = defaultdict(int)
        max_freq = 0
        best = 0

        for r in range(len(s)):
            freq_map[s[r]] += 1
            max_freq = max(max_freq, freq_map[s[r]])

            if (r - l + 1) - max_freq > k:
                freq_map[s[l]] -= 1
                l += 1

            best = max(best, r - l + 1)

        return best


s = "AABABBA"
k = 1 # 4
# s = "ABAB" 
# k = 2 # 4
# s = "XYYX" 
# k = 2 # 4
# s = "AAABABB"
# k = 1 # 5

print(Solution().characterReplacement(s,k))  
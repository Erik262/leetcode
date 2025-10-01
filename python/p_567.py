from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        freq_s1 = Counter(s1)

        l = 0

        for r in range(len(s1), len(s2) + 1):
            freq_s2 = Counter(s2[l:r])
            if freq_s1 == freq_s2:
                return True

            l += 1

        return False

# s1 = "aab"
# s2 = "aabaabaab" # True

# s1="hello"
# s2="ooolleoooleh" # False

# s1 = "abc"
# s2 = "lecabee" # True

# s1 = "abc"
# s2 = "lecaabee" # False

# s1="ab"
# s2="lecabee" # True

s1 = "ab"
s2 = "eidbaooo" # True

# s1 = "ab"
# s2 = "eidboaoo" # False

print(Solution().checkInclusion(s1,s2))  
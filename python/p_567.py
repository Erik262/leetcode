class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        
        s1_counter = [0] * 26
        s2_counter = [0] * 26
        matches = 0
        l = 0

        for i in range(len(s1)): # a = 97, b = 98
            # to become 'a' indexed as 0, 'b' as 1, 'c' as 2 etc...
            s1_counter[ord(s1[i]) - ord("a")] += 1 
            s2_counter[ord(s2[i]) - ord("a")] += 1

        for i in range(26):
            if s1_counter[i] == s2_counter[i]:
                matches += 1

        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            idx = ord(s2[r]) - ord('a')
            s2_counter[idx] += 1 # next character in our sliding window

            if s1_counter[idx] == s2_counter[idx]:
                matches += 1

            elif s1_counter[idx] + 1 == s2_counter[idx]:
                matches -= 1

            idx = ord(s2[l]) - ord('a')
            s2_counter[idx] -= 1

            if s1_counter[idx] == s2_counter[idx]:
                matches += 1

            elif s1_counter[idx] - 1 == s2_counter[idx]:
                matches -= 1

            l += 1

        return matches == 26


        









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
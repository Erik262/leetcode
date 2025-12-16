class Solution:
    def isPalindrome(self, s):
        s = "".join(char for char in s if char.isalnum()).lower()
        s_n = len(s)

        for c in range(s_n // 2):
            if s[c] != s[s_n - c - 1]:
                return False
            
        return True

# s = "Was it a car or a cat I saw?" # True
# s = "tab a cat" # False
# s = "A man, a plan, a canal: Panama" # True
# s = "race a car" # False
s = " " # True

print(Solution().isPalindrome(s))
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        pt = "()" * n
        perm = 1

        for i in range(1, n + 1):
            perm *= i


        for i in perm:
            pass






# n = 1
# Output: ["()"]

n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

print(Solution().generateParenthesis(n))
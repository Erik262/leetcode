class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        result = []

        def dfs(n_open: int, n_close: int):
            if n_open == n_close == n:
                result.append("".join(stack))
                return

            if n_open < n:
                stack.append('(')
                dfs(n_open + 1, n_close)
                stack.pop()

            if n_close < n_open:
                stack.append(')')
                dfs(n_open, n_close + 1)
                stack.pop()

        dfs(0,0)
        return result
        
# n = 1
# Output: ["()"]

n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

print(Solution().generateParenthesis(n))
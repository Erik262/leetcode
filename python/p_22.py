class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        result = []

        def recursive(n_open, n_closed):
            if n_open == n_closed == n:
                result.append("".join(stack))
                return
            
            if n_open < n:
                stack.append("(")
                recursive(n_open + 1, n_closed)
                stack.pop()

            if n_closed < n_open:
                stack.append(")")
                recursive(n_open, n_closed + 1)
                stack.pop()

        recursive(0,0)

        return result
        
# n = 1
# Output: ["()"]

n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

print(Solution().generateParenthesis(n))
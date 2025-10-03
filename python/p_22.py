class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = [("", n, n)]
        result = []

        while stack:
            curr, open_left, close_left = stack.pop()

            if open_left == 0 and close_left == 0:
                result.append(curr)
                continue

            if open_left > 0:
                stack.append((curr + "(", open_left - 1, close_left))
            
            if close_left > open_left:
                stack.append((curr + ")", open_left, close_left - 1))

        return result
        
# n = 1
# Output: ["()"]

n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

print(Solution().generateParenthesis(n))
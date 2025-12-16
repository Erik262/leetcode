class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        operator = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y),
            }

        for t in tokens:
            if t in operator:
                y = stack.pop()
                x = stack.pop()
                result = operator[t](x,y)
                stack.append(result)
            else:
                stack.append(int(t))

        return stack.pop()

# tokens = ["2","1","+","3","*"]
# Output: 9

# tokens = ["18"]
# Output: 18

# tokens = ["4","13","5","/","+"]
# Output: 6

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22

print(Solution().evalRPN(tokens))
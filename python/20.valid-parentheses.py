class Solution(object):
    def isValid(self, s):
        stack = []
        for c in s:
            match c:
                case ')':
                    if (len(stack) != 0) and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                case '}':
                    if (len(stack) != 0) and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                case ']':
                    if (len(stack) != 0) and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                case _:
                    stack.append(c)
        return len(stack) == 0

# s = "()" # True
# s = "()[]{}" # True
# s = "(]" # False
# s = "([])" # True
# s = "]]" # False
s = "(])(])" # False
# s = ")" # False
# s = "(" # False
    
print(Solution().isValid(s))
#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        result = [0] * (n1 + n2)
        fin = ""

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):

                mul = int(num1[i]) * int(num2[j])
                sum_ = mul + result[i + j + 1]

                result[i + j + 1] = sum_ % 10
                result[i + j] += sum_ // 10

        k = 0
        while k < len(result) and result[k] == 0:
            k += 1
        fin = "0" if k == len(result) else "".join(str(d) for d in result[k:])

        return fin



num1 = "3" # "12"
num2 = "4"

num1 = "111" # "24642"
num2 = "222"

num1 = "123" # "56088"
num2 = "456"

print(Solution().multiply(num1, num2))

        
# @lc code=end


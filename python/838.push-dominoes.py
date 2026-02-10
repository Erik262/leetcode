#
# @lc app=leetcode id=838 lang=python3
#
# [838] Push Dominoes
#

# @lc code=start
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        arr = list("L" + dominoes + "R")
        n = len(arr)

        i = 0

        for j in range(1, n):
            if arr[j] == '.':
                continue

            # L...L or R...R
            if arr[i] == arr[j]:
                for k in range(i + 1, j):
                    arr[k] = arr[i]

            elif arr[i] == 'R' and arr[j] == 'L':
                left, right = i+1, j-1

                while left < right:
                    arr[left] = 'R'
                    arr[right] = 'L'

                    left += 1
                    right -= 1

            i = j

        return "".join(arr[1:-1])
        
# @lc code=end


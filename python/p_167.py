class Solution:
    def twoSum(self, numbers, target):
        l_idx = 0
        r_idx = len(numbers) - 1

        while l_idx < r_idx:
            l_v = numbers[l_idx]
            r_v = numbers[r_idx]

            if (l_v + r_v == target):
                return [l_idx + 1, r_idx + 1]

            if (l_v + r_v) > target:
                r_idx -= 1
            else:
                l_idx += 1



numbers = [2,7,11,15] # [1,2]
target = 9

# numbers = [0, 0, 3, 4] # [1,2]
# target = 0

# numbers = [0,2,3,4,8,9,11] # [2,5]
# target = 10

# numbers = [2,3,4] # [1,3]
# target = 6

# numbers = [-1,0] # [1,2]
# target = -1

# numbers = [1,2,3,4] # [1,2]
# target = 3

print(Solution().twoSum(numbers, target))
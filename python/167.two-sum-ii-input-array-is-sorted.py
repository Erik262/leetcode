class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1

        while left < right:
            res = numbers[left] + numbers[right]

            if res < target:
                left += 1
            elif res > target:
                right -= 1
            else:
                return [left + 1, right + 1]



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
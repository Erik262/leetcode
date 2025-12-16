class Solution:
    def longestConsecutive(self, nums):
        counter = 0
        best = []

        if len(nums) == 0:
            best.append(counter)
            return counter

        s_nums = sorted(nums)
        for idx, n in enumerate(s_nums):
            if idx == 0:
                counter += 1
                best.append(counter)
                continue
            diff = abs(n - s_nums[idx - 1])
            if diff == 1:
                counter += 1
                best.append(counter)

            if diff > 1:
                counter = 1

        return max(best)


nums = [2, 20, 4, 10, 3, 4, 5]  # 4
# nums = [0,-1] # 2
# nums = [9,1,4,7,3,-1,0,5,8,-1,6] # 7
# nums = [9,1,4,7,3,-1,0,5,8,-1,6] # 7
# nums = [0]

print(Solution().longestConsecutive(nums))

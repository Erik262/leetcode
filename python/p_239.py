from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):

        d = deque()
        arr = []
        max_idx = 0
        
        for idx in range(len(nums)):
            while (len(d) != 0) and (nums[d[-1]] < nums[idx]):
                d.pop()
            d.append(idx)

            if idx >= k - 1:
                max_idx = d[0]
                if (idx - k) < max_idx:
                    arr.append(nums[max_idx])
                else:
                    arr.append(nums[d[1]])
                    d.popleft()

        return arr

nums = [1,3,-1,-3,5,3,6,7]
k = 3 # [3,3,5,5,6,7]

# nums=[1,2,1,0,4,2,6]
# k=3 # [2, 2, 4, 4, 6]

# nums = [1]
# k = 1 # [1]

print(Solution().maxSlidingWindow(nums,k))
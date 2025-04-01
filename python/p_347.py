class Solution(object):
    def topKFrequent(self, nums, k):

        h_map = {}
        for n in nums:
            if n in h_map:
                h_map[n] += 1
            else:
                h_map[n] = 1
        
        h_map = sorted(h_map.items(), key=lambda x: x[1], reverse=True)[:k]

        new_map = []
        for (a,b) in h_map:
            new_map.append(a)

        return new_map



# nums = [1,2,2,3,3,3,4]
nums = [1,9,9,9,3,2,3,4]
k = 2
print(Solution().topKFrequent(nums,k))        
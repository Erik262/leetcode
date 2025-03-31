class Solution(object):
    def containsDuplicate(self, nums):

        h_map = {} # key : index

        for idx, n in enumerate(nums):

            if n in h_map:
                return True
            
            h_map[n] = idx

        return False

nums = [1,2,3,0]

print(Solution().containsDuplicate(nums))
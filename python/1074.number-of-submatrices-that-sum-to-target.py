#
# @lc app=leetcode id=1074 lang=python3
#
# [1074] Number of Submatrices That Sum to Target
#
from collections import defaultdict

# @lc code=start
class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        row_sums = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                top = row_sums[r-1][c] if r > 0 else 0
                left = row_sums[r][c-1] if c > 0 else 0
                top_left = row_sums[r-1][c-1] if min(r,c) > 0 else 0

                row_sums[r][c] = matrix[r][c] + top + left - top_left

        res = 0
        for r1 in range(rows):
            for r2 in range(r1, rows):
                cnt = defaultdict(int)
                cnt[0] = 1

                for c in range(cols):
                    cur_sum = row_sums[r2][c] - (row_sums[r1-1][c] if r1 > 0 else 0)
                    diff = cur_sum - target
                    res += cnt[diff]
                    cnt[cur_sum] += 1

        return res
# @lc code=end


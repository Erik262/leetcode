from typing import List
from collections import defaultdict, Counter
# @lc app=leetcode id=2013 lang=python3
#
# [2013] Detect Squares
#

# @lc code=start
class DetectSquares:

    def __init__(self):
        self.row = defaultdict(Counter)
        self.cnt = Counter()

    def add(self, point: List[int]) -> None:
        x, y = point

        self.row[y][x] += 1
        self.cnt[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        qx, qy = point
        total = 0

        for x, freq in self.row[qy].items():
            if x == qx:
                continue

            dist = abs(qx - x)
            y1, y2 = qy + dist, qy - dist

            # Top
            total += freq * self.cnt.get((qx, y1), 0) * self.cnt.get((x, y1), 0)

            # Bottom
            total += freq * self.cnt.get((qx, y2), 0) * self.cnt.get((x, y2), 0)

        return total

# Input
# ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
# [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
# Output
# [null, null, null, null, 1, 0, null, 2]


detectSquares = DetectSquares()
detectSquares.add([3, 10])
detectSquares.add([11, 2])
detectSquares.add([3, 2])
detectSquares.count([11, 10])  # return 1. You can choose:
#                                #   - The first, second, and third points
detectSquares.count([14, 8])   # return 0. The query point cannot form a square with any points in the data structure.
detectSquares.add([11, 2])     # Adding duplicate points is allowed.
detectSquares.count([11, 10])  # return 2. You can choose:
                               #   - The first, second, and third points
                               #   - The first, third, and fourth points

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
# @lc code=end


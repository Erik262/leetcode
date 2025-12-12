from typing import List
from collections import defaultdict

# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        smap = defaultdict(list)
        result = []
        tickets.sort(reverse=True)

        for f, t in tickets:
            smap[f].append(t)

        def dfs(f):
            while smap[f]:
                to = smap[f].pop()
                dfs(to)
            result.append(f)

        dfs("JFK")

        return result[::-1]


# tickets = [["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]
# Output: ["JFK","BUF","HOU","SEA"]

# tickets = [["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]
# Output: ["JFK","HOU","JFK","SEA","JFK"]

tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# ["JFK","MUC","LHR","SFO","SJC"]

print(Solution().findItinerary(tickets))      
# @lc code=end


#
# @lc app=leetcode id=2353 lang=python3
#
# [2353] Design a Food Rating System
#
from typing import List
from collections import defaultdict
import heapq
# @lc code=start
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_map = {}
        self.cuisines_map = defaultdict(list)

        for i in range(len(foods)):
            self.food_map[foods[i]] = (cuisines[i], ratings[i])
            self.cuisines_map[cuisines[i]].append((-ratings[i], foods[i]))

        for c in self.cuisines_map:
            heapq.heapify(self.cuisines_map[c])

    def changeRating(self, food: str, newRating: int) -> None:
        if food in self.food_map:
            cuis, _ = self.food_map[food]
            self.food_map[food] = (cuis, newRating)
            heapq.heappush(self.cuisines_map[cuis], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisines_map[cuisine]

        while True:
            rating, food = heap[0]
            if self.food_map[food][1] == -rating:
                return food
                
            heapq.heappop(heap)
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
# @lc code=end


#
# @lc app=leetcode id=1396 lang=python3
#
# [1396] Design Underground System
#
from collections import defaultdict
# @lc code=start

class UndergroundSystem:

    def __init__(self):
        self.traveling = {}
        self.trip = defaultdict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.traveling:
            return None
        else:
            self.traveling[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.traveling:
            start_station, start_time = self.traveling[id]
            data = self.trip.get((start_station, stationName), [0, 0])
            data[0] += (t - start_time)
            data[1] += 1

            self.trip[(start_station, stationName)] = data

            del self.traveling[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        data = self.trip[(startStation, endStation)]
        time = data[0] / data[1]

        return time
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# @lc code=end


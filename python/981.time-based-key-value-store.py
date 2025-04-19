#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
class TimeMap:
    def __init__(self):
        self.hmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hmap:
            self.hmap[key] = []
        self.hmap[key].append([timestamp, value])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap:
            return ""
        selected = self.hmap[key]

        l = 0
        r = len(selected) - 1
        while l <= r:
            m = (l + r) // 2
            if timestamp < selected[m][0]:
                r = m - 1
            elif timestamp > selected[m][0]:
                l = m + 1
            else:
                return selected[m][1]
            
        if r >= 0:
            return selected[r][1]
        else:
            return ""


input = ["TimeMap", "set", "get", "get", "set", "get", "get"] 
input = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
output = [None, None, "bar", "bar", None, "bar2", "bar2"]

obj = TimeMap() # None
obj.set("foo", "bar", 1) # None
obj.set("fubu", "bar", 2) # None

# obj.get("foo", 1) # "bar"
# obj.get("foo", 3) # "bar"

obj.set("foo", "bar2", 2) # None
obj.set("foo", "bar3", 3) # None
obj.set("foo", "bar4", 4) # None
obj.set("foo", "bar5", 5) # None

# obj.get("foo", 1) # "bar2"
# obj.get("foo", 5) # "bar2"

# param_2 = obj.get()

print(obj.get("fooi", 1))

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end


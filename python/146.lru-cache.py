#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start

class ListNode:
    def __init__(self, key=0, value=0, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_front(self, node: ListNode):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _pop_back(self) -> ListNode:
        popped = self.tail.prev
        self._remove(popped)

        return popped
        
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]
        self._remove(node)
        self._add_front(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._remove(self.map[key])
            del self.map[key]

        if len(self.map) >= self.cap:
            popped_node = self._pop_back()
            del self.map[popped_node.key]
        
        node = ListNode(key, value)
        self._add_front(node)
        self.map[key] = node


# Input: ["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]
# Output: [null, null, 10, null, null, 20, -1]

# Your LRUCache object will be instantiated and called as such:

lRUCache = LRUCache(2)
lRUCache.put(1, 10)  # cache: {1=10}
lRUCache.get(1)      # return 10
lRUCache.put(2, 20)  # cache: {1=10, 2=20}
lRUCache.put(3, 30)  # cache: {2=20, 3=30}, key=1 was evicted
lRUCache.get(2)      # returns 20 
lRUCache.get(1)      # return -1 (not found)



# @lc code=end


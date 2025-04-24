#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start

class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    
    def _add_to_front(self, node: ListNode) -> None:
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _remove_from_tail(self) -> ListNode:
        removed_node = self.tail.prev
        self._remove_node(self.tail.prev)

        return removed_node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove_node(node)
            self._add_to_front(node)

            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove_node(self.cache[key])
            del self.cache[key]

        if len(self.cache) >= self.capacity:
            rev_node = self._remove_from_tail()
            del self.cache[rev_node.key]

        node = ListNode(key,value)
        self._add_to_front(node)
        self.cache[key] = node


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


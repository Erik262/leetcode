from typing import Optional, List
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = head
        f = head

        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
            
        return False

def list_to_linkedlist(items: List[int]) -> Optional[ListNode]:
    if not items:
        return None
    tail = ListNode(items[0])
    curr = tail
    for val in items[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return tail

def linkedlist_to_list(tail: Optional[ListNode]) -> List[int]:
    result = []
    while tail:
        result.append(tail.val)
        tail = tail.next
    return result


head = [3,2,0,-4] # True
# pos = 1

# head = [1,2] # True
# pos = 0

# head = [1] # False
# pos = -1

print(Solution().hasCycle(list_to_linkedlist(head)))

        
# @lc code=end


from typing import List, Optional
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        for i in range(1, len(lists)):
            lists[i] = self._merge(lists[i - 1], lists[i])
        
        return lists[-1]

    def _merge(self, l1, l2):
        head = ListNode()
        tail = head

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
                tail = tail.next

            elif l1.val > l2.val:
                tail.next = l2
                l2 = l2.next
                tail = tail.next
            else:
                tail.next = l1
                l1 = l1.next
                tail = tail.next

        # If one list becomes empty
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return head.next

def list_to_linkedlist(items: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    for val in items:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linkedlist_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


lists = [[1,4,5],[1,3,4],[2,6]] # [1,1,2,3,4,4,5,6]

# lists = [] # []

# lists = [[]] # []
# lists = [[1]] # []

llists = [list_to_linkedlist(xs) for xs in lists]
res = Solution().mergeKLists(llists)
print(linkedlist_to_list(res))
        
# @lc code=end


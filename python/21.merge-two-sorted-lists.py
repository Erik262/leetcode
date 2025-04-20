from typing import Optional, List
#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2

        dummy = ListNode()
        tail = dummy

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                tail.next = curr1
                curr1 = curr1.next
                tail = tail.next
                
            else:
                tail.next = curr2
                curr2 = curr2.next
                tail = tail.next

        tail.next = curr1 or curr2

        return dummy.next

list1 = [1,2,4] # [1,1,2,3,4,4]
list2 = [1,3,4]

# list1 = [] # []
# list2 = []

# list1 = [] # []
# list2 = [0]


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

sol = Solution().mergeTwoLists(list_to_linkedlist(list1), list_to_linkedlist(list2))

# while sol:
#     print(sol.val)
#     sol = sol.next
        
# @lc code=end


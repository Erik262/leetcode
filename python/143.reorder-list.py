from typing import Optional, List
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half list
        second = slow.next
        prev = None
        slow.next = None
        while second:
            _second_next = second.next
            second.next = prev
            prev = second
            second = _second_next
            
        # merge both together
        first = head
        second = prev
        while second:
            _first_next = first.next
            _second_next = second.next

            first.next = second
            second.next = _first_next

            first = _first_next
            second = _second_next

        # while head:
        #     print(head.val)
        #     head = head.next

        

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


# head = [1,2,3,4] # [1,4,2,3]
# head = [1,2,3,4,5] # [1,5,2,4,3]

head = [1,2,3,4,5,6,7,8,9]

Solution().reorderList(list_to_linkedlist(head))



# @lc code=end


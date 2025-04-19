from typing import Optional, List
#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            _curr_next = curr.next
            curr.next = prev
            prev = curr 
            curr = _curr_next

        return prev
    



# Helper function to run own test examples

def list_to_linkedlist(items: List[int]) -> Optional[ListNode]:
    if not items:
        return None
    head = ListNode(items[0])
    curr = head
    for val in items[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def linkedlist_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result




head = [1,2,3,4,5]

ll_head = list_to_linkedlist(head)
reversed_ll = Solution().reverseList(ll_head)

print(linkedlist_to_list(reversed_ll))

# @lc code=end


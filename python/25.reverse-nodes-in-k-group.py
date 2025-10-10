from typing import Optional, List
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def has_k(self, group_head: Optional[ListNode], k: int):
        curr = group_head
        for _ in range(k):
            if curr is None:
                return False, None
            curr = curr.next
        return True, curr

    def reverse_segment(self, start, tail_next):
        prev = tail_next
        curr = start
        while curr != tail_next:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev, start

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_group_tail = dummy
        group_head = head

        while True:
            has_full, tail_next = self.has_k(group_head, k)
            if not has_full:
                break
            
            new_head, new_tail = self.reverse_segment(group_head, tail_next)
            prev_group_tail.next = new_head
            new_tail.next = tail_next

            prev_group_tail = new_tail
            group_head = tail_next

        return dummy.next



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

# head = [1,2,3,4,5] # [3,2,1,6,5,4]
# k = 3

head = [1,2,3,4,5] # [3,2,1,4,5]
k = 3


res = Solution().reverseKGroup(list_to_linkedlist(head), k)
print(linkedlist_to_list(res))
        
# @lc code=end


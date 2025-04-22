from typing import Optional, List
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        f_counter = 1
        while fast:
            fast = fast.next
            if f_counter > n:
                slow = slow.next
            f_counter += 1

        slow.next = slow.next.next

        return dummy.next


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



head = [1,2,3,4,5] # [1,2,3,5]
n = 2

# head=[1,2,3,4] # [1,2,4]
# n=2


# head = [1] # []
# n = 1

# head = [1,2] # [1]
# n = 1


res = Solution().removeNthFromEnd(list_to_linkedlist(head), n)

print(linkedlist_to_list(res))
        
# @lc code=end


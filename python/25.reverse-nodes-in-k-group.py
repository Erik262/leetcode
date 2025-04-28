from typing import Optional, List
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        group = dummy

        while True:
            curr = self.check_k_nodes(group.next, k)
            if not curr:
                break

            group_start = group.next
            group_end = curr
            next_group_start = curr.next

            # reverse
            prev = next_group_start
            curr = group_start
            while curr != next_group_start:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            temp = group.next
            group.next = group_end
            temp.next = next_group_start
            group = temp

        return dummy.next


    def check_k_nodes(self, curr, k):
        while curr and k > 1:
            curr = curr.next
            k -= 1
        return curr



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


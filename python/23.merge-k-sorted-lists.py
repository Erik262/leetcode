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
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        head = ListNode()
        curr = head
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
            
        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        if len(lists) == 1:
            return lists[0]
            
        mid = len(lists) // 2
        left_merged = self.mergeKLists(lists[:mid])
        right_merged = self.mergeKLists(lists[mid:])
        
        return self.mergeTwoLists(left_merged, right_merged)

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


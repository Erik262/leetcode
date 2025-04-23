from typing import Optional, List
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        number1 = 0
        number2 = 0

        n1 = []
        n2 = []

        sum = 0

        while l1:
            n1.insert(0,l1.val)
            l1 = l1.next

        while l2:
            n2.insert(0,l2.val)
            l2 = l2.next

        for n in n1:
            number1 = (number1 * 10) + n

        for n in n2:
            number2 = (number2 * 10) + n

        sum = str(number1 + number2)

        res_node = dummy
        for s in reversed(sum):
            node = ListNode(int(s))
            res_node.next = node
            res_node = res_node.next

        res_node.next = None

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


l1 = [2,4,3] # [7,0,8]
l2 = [5,6,4]

# l1 = [0] # [0]
# l2 = [0]

# l1 = [9,9,9,9,9,9,9] # [8,9,9,9,0,0,0,1]
# l2 = [9,9,9,9]


res = Solution().addTwoNumbers(list_to_linkedlist(l1),list_to_linkedlist(l2))

print(linkedlist_to_list(res))

# @lc code=end


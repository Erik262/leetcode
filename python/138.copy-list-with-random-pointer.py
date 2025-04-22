from typing import Optional, List
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        dummy = Node(x=0,next=head,random=None)

        _head = head
        while _head:
            org_next = _head.next
            new_node = Node(x=_head.val)
            _head.next = new_node # insert cloned in our list kinda a 'zip'
            new_node.next = org_next
            _head = new_node.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next # curr.next is our clone
            curr = curr.next.next # skip clone node

        curr = head
        copy_ = dummy
        while curr:
            copy = curr.next
            curr.next = copy.next # skipping over our copy/clone
            copy_.next = copy
            copy_ = copy
            
            curr = curr.next

        return dummy.next




def list_to_ll(data: List[List[Optional[int]]]) -> Optional[Node]:
    if not data: return None
    nodes = [Node(x) for x, _ in data]
    for i, (_, r) in enumerate(data):
        if i < len(nodes) - 1: nodes[i].next = nodes[i + 1]
        nodes[i].random = nodes[r] if r is not None else None
    return nodes[0]

def ll_to_list(h: Optional[Node]) -> List[List[Optional[int]]]:
    m, out, cur, idx = {}, [], h, 0
    while cur: m[cur] = idx; cur = cur.next; idx += 1
    cur = h
    while cur:
        out.append([cur.val, m[cur.random] if cur.random in m else None]); cur = cur.next
    return out

def print_ll(h: Optional[Node]) -> None:
    m, cur, idx = {}, h, 0
    while cur: m[cur] = idx; cur = cur.next; idx += 1
    cur = h
    while cur:
        print(f"Node[{m[cur]}]: val={cur.val}, random->{m.get(cur.random)}"); cur = cur.next


head = [[7,None],[13,0],[11,4],[10,2],[1,0]] # [[7,None],[13,0],[11,4],[10,2],[1,0]]
# head = [[1,1],[2,1]] # [[1,1],[2,1]]
# head = [[3,None],[3,0],[3,None]] # [[3,None],[3,0],[3,None]]

res = Solution().copyRandomList(list_to_ll(head))
print_ll(res)
        
# @lc code=end


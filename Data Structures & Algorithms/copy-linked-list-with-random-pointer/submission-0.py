"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        has_map = {None:None}
        #first copy all nodes. 
        cur = head
        while cur:
            has_map[cur] = Node(cur.val)
            cur = cur.next
        #self.random is also a node present so we can use that
        cur = head
        while cur:
            copy = has_map[cur]
            copy.next = has_map[cur.next]
            copy.random = has_map[cur.random]
            cur = cur.next
        return has_map[head]
        
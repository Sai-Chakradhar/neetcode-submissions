"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        from collections import deque
        if not node:
            return None

        visited = {}

        visited[node] = Node(node.val)

        queue = deque([node])

        while queue:
            node_1 = queue.popleft()
            for n in node_1.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val)
                    queue.append(n)
                visited[node_1].neighbors.append(visited[n])
        return visited[node]

        
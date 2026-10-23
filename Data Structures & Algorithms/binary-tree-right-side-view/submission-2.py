# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = deque([root])
        list_2 = []
        while queue:
            right_node = None
            for i in range(len(queue)):
                print(i)
                node = queue.popleft()
                right_node = node
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            if right_node:
                list_2.append(right_node.val)

        return list_2
                
        
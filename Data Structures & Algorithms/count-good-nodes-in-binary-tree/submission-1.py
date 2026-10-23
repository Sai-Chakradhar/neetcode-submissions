# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([(root, root.val)])
        count = 0
        while queue:
            node, maxValue = queue.popleft()
            if node.val>=maxValue:
                count+=1
            newmaxx = max(maxValue, node.val)
            if node.left:
                queue.append((node.left,newmaxx))
            if node.right:
                queue.append((node.right,newmaxx))
        return count
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        row , column = len(grid), len(grid[0])
        queue = deque()
        for r in range(0,row):
            for c in range(0,column):
                if grid[r][c]==0:
                    queue.append((r,c))
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            r,c = queue.popleft()
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                if (0<=nr<row and 
                0<=nc<column and
                grid[nr][nc]==2147483647):

                    grid[nr][nc] = grid[r][c]+1
                    queue.append((nr,nc))


        
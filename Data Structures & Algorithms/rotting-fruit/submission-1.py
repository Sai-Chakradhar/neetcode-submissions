class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        row, column = len(grid),len(grid[0])
        queue = deque()
        fresh = 0
        minutes = 0
        for r in range(row):
            for c in range(column):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh +=1


        while queue and fresh>0:
            for _ in range(len(queue)):
                directions = [[0,1],[-1,0],[0,-1],[1,0]]
                r,c = queue.popleft()
                for dr, dc in directions:
                    nr = r+dr
                    nc = c+dc
                    if(0<=nr<row and
                    0<=nc<column and
                    grid[nr][nc] ==1):
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        fresh -=1
                    
            minutes +=1

        if fresh ==0:
            return minutes
        
        return -1



        
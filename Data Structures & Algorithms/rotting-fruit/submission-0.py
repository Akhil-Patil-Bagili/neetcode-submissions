class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = collections.deque()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        res=0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append((row,col))
        
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr<0 or nr>=ROWS or nc<0 or nc>=COLS or grid[nr][nc]!=1:
                        continue

                    queue.append((nr,nc))
                    grid[nr][nc] = 2
            res+=1

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return -1
        return max(0,res-1)

        
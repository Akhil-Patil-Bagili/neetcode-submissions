class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = collections.deque()
        visited = set()

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row,col))
                    visited.add((row,col))
        
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr<0 or nr >= ROWS or nc<0 or nc >= COLS or (nr,nc) in visited or grid[nr][nc] != 2147483647:
                    continue
                
                grid[nr][nc] = grid[r][c] + 1
                visited.add((nr,nc))
                queue.append((nr,nc))

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxArea = 0
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]!=1 or (r,c) in visited:
                return 0
            
            visited.add((r,c))

            area = 1
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row,col) not in visited:
                    maxArea = max(maxArea, dfs(row, col))
        return maxArea
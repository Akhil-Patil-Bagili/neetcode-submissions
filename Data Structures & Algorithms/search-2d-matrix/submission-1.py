class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        low, high = 0, ROWS*COLS - 1

        while low <= high:
            mid = (low+high)//2

            row = mid // COLS
            col = mid % COLS

            value = matrix[row][col]

            if value == target:
                return True
            
            elif value < target:
                low = mid + 1
            
            else:
                high = mid - 1
            
        return False
        

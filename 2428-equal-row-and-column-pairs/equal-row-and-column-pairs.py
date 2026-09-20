class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        count =0
        cols=[]
        for col in range(len(grid)):
            column = []

            for row in range(len(grid)):
                column.append(grid[row][col])
            cols.append(column)  
        
        for i in grid:
            for j in cols:
                if i == j:
                    count +=1
        return count

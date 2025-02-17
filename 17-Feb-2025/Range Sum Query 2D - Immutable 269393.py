# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if row == 0:
                    if column > 0:
                        self.matrix[row][column] += self.matrix[row][column - 1] 
                else:
                    if column > 0:
                        self.matrix[row][column] += self.matrix[row][column - 1] + self.matrix[row-1][column] - self.matrix[row - 1][column - 1] 
                    else:
                        self.matrix[row][column] += self.matrix[row - 1][column]
                    


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 > 0 and col1 > 0:
            return self.matrix[row2][col2] - self.matrix[row2][col1 - 1] - self.matrix[row1 - 1][col2] + self.matrix[row1 - 1][col1- 1]
        if row1 == 0:
            if col1 == 0:
                return self.matrix[row2][col2]
            return self.matrix[row2][col2] - self.matrix[row2][col1 - 1] 
        if col1 == 0:
            if row1 == 0:
                return self.matrix[row][col2]
            return self.matrix[row2][col2] - self.matrix[row1 - 1][col2]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
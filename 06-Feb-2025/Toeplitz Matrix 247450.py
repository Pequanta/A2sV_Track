# Problem: Toeplitz Matrix - https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        #lower

        for start_row in range(len(matrix)):
            row = start_row
            column = 0
            element = matrix[start_row][0]
            first_time = True
            while column < len(matrix[0]) and row < len(matrix):
                if not first_time:
                    if matrix[row][column] != element:
                        return False
                else:
                    first_time = False
                row += 1
                column += 1
        #upper
        for start_column in range(len(matrix[0])):
            column = start_column
            row = 0
            element = matrix[0][start_column]
            while column < len(matrix[0]) and row < len(matrix):
                if not first_time:
                    if matrix[row][column] != element:
                        return False
                else:
                    first_time = False
                row += 1
                column += 1
        return True


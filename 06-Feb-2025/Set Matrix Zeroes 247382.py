# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix_copy = [[0] * len(matrix[0]) for _ in range(len(matrix))]


        for a in range(len(matrix)):
            for b in range(len(matrix[0])):
                matrix_copy[a][b] = matrix[a][b]
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix_copy[row][column] == 0:
                    for i in range(len(matrix)):
                        matrix[i][column] = 0
                    for j in range(len(matrix[0])):
                        matrix[row][j] = 0
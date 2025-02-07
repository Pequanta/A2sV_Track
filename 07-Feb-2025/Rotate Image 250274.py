# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


        temp_matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                temp_matrix[i][j] = matrix[i][j]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = temp_matrix[j][i] 
        
        for row in range(len(matrix)):
            matrix[row] = matrix[row][::-1]
        return matrix
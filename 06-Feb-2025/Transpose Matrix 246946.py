# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        start_index = 0
        transposed_matrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                transposed_matrix[j][i] = matrix[i][j]
        return transposed_matrix        
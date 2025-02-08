# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        result = []

        dx_dy = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, -1), (1, 1), (-1, -1)]

        def check_validity(row, column , direction):
            temp_point = [direction[0] + row, direction[1] + column]
            if (temp_point[0] < len(grid) and temp_point[1] < len(grid[0])) and (temp_point[0] >= 0 and temp_point[1] >= 0):
                return True
            return False
        for row in range(len(grid)):
            temp_cont = []
            for column in range(len(grid)):
                flag = True
                max_val = grid[row][column]
                for direction in dx_dy:
                    if not check_validity(row, column , direction):
                        flag = False
                        break
                    max_val = max(max_val, grid[row + direction[0]][column + direction[1]])
                if flag:
                    temp_cont.append(max_val)
            if len(temp_cont) != 0:
                result.append(temp_cont)
        return result
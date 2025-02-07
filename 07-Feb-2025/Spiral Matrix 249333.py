# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited_points = set()
        dx_dy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        current_step = 0
        current_point = [0, 0]
        result = []
        count_visited = 0
        row = len(matrix)
        column = len(matrix[0])
        def check_validity(point):
            if (point[0] < row and point[1] < column) and (point[0] > -1 and point[1] > -1):
                return True
            return False
        temp_point = (0, 0)
        while count_visited < (row * column):
            if check_validity(temp_point) and (temp_point not in visited_points):
                visited_points.add(temp_point)
                current_point = temp_point
                result.append(matrix[temp_point[0]][temp_point[1]])
                count_visited += 1
            else:
                current_step += 1
            temp_point = (current_point[0] + dx_dy[current_step % 4][0], current_point[1] + dx_dy[current_step % 4][1])
        return result


            


            

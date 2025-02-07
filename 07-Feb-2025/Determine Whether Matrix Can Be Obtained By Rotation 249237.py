# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        rot_row = 0
        rot_column = 0
        first_check = True
        second_check = True
        third_check = True
        
        for column in range(len(target)):
            rot_column = 0
            for row in range(len(target[0]) - 1, -1, -1):
                if mat[row][column] != target[rot_row][rot_column]:
                    first_check = False
                    break
                rot_column += 1
            rot_row += 1
        rot_row = len(target) - 1
        for row in range(len(mat)):
            rot_column = len(target[0]) - 1
            for column in range(len(mat[0])):
                if mat[row][column] != target[rot_row][rot_column]:
                    second_check = False
                    break
                rot_column -= 1
            rot_row -= 1
        rot_column = 0
        for row in range(len(mat)):
            rot_row = len(mat) - 1
            for column in range(len(mat[0])):
                if mat[row][column] != target[rot_row][rot_column]:
                    third_check = False
                    break
                rot_row -= 1
            rot_column += 1
        fourth_check = True
        for row in range(len(mat)):
            for column in range(len(mat)):
                if mat[row][column] != target[row][column]:
                    fourth_check = False
                    break
        return first_check or second_check or third_check or fourth_check
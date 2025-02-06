# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        current_set = set()
        def check_blocks(row, column):
            block_set = set()
            for i in range(row, row + 3):
                for j in range(column, column + 3):
                    if board[i][j] in block_set:
                        return False
                    if board[i][j].isdigit():
                        block_set.add(board[i][j])
            return True
        #row cheeck
        for row in range(len(board)):
            current_set.clear()
            for column in range(len(board[0])):
                if board[row][column] in current_set:
                    return False
                elif board[row][column].isdigit():
                    current_set.add(board[row][column])

        #column check
        for column in range(len(board[0])):
            current_set.clear()
            for row in range(len(board)):
                if board[row][column] in  current_set:
                    return False
                if board[row][column].isdigit():
                    current_set.add(board[row][column])
        #block check
        for row in range(0, len(board), 3):
            for column in range(0, len(board), 3):
                if not check_blocks(row, column):
                    return False
        return True
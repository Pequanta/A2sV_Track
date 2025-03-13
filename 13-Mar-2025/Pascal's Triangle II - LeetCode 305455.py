# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def helper(numRow, arr):
            if numRow == 0:
                return arr
            i = 1
            prev = 1
            while i < len(arr):
                temp = arr[i]
                arr[i] += prev
                prev = temp
                i += 1
            arr.append(1)
            numRow -= 1
            return helper(numRow, arr)
        return helper(rowIndex, [1])


                
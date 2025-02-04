# Problem: Final Value of Variable After Performing Operations - https://leetcode.com/problems/final-value-of-variable-after-performing-operations

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for symbol in operations:
            if "+" in symbol:
                x += 1
            else:
                x -= 1
        return x
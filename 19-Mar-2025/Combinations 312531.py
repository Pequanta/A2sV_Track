# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def helper(start_num , temp_result):
            if len(temp_result) == k:
                result.append(temp_result[:])
                return
            for i in range(start_num, n + 1):
                temp_result.append(i)
                helper(i + 1, temp_result)
                temp_result.pop()
            return result
        helper(1 , [])
        return result
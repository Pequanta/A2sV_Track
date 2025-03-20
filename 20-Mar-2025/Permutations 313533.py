# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtracking(start_num, temp_result):
            nonlocal result
            if len(temp_result) == len(nums):
                result.append(temp_result[:])
                return 

            for i in range(len(nums)):
                if nums[i] not in temp_result:
                    temp_result.append(nums[i])
                    backtracking(i + 1, temp_result)
                    temp_result.pop()

        backtracking(0, [])
        return result

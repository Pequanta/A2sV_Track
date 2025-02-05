# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        cont_evens = [nums[i] for i in range(len(nums)) if nums[i] % 2 == 0]
        current_sum= sum(cont_evens)
        result = []
        for i in range(len(queries)):
            if nums[queries[i][1]] % 2 == 0:
                if queries[i][0] % 2 != 0:
                    current_sum -= nums[queries[i][1]]
                    nums[queries[i][1]] += queries[i][0]
                    result.append(current_sum)
                else:
                    current_sum += queries[i][0]
                    nums[queries[i][1]] += queries[i][0]
                    result.append(current_sum)
            else:
                if queries[i][0] % 2 != 0:
                    current_sum += queries[i][0] + nums[queries[i][1]]
                    result.append(current_sum)
                    nums[queries[i][1]] = queries[i][0] + nums[queries[i][1]]
                else:
                    nums[queries[i][1]] += queries[i][0]
                    result.append(current_sum)
        return result
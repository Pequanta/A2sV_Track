# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = [0] * (len(nums) + 1)
        cont_pre_sums = Counter({0: 1})
        count = 0
        for i in range(1, len(pre_sum)):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]
            count += cont_pre_sums[pre_sum[i] - k]
            cont_pre_sums[pre_sum[i]] += 1
        return count
            
            
        
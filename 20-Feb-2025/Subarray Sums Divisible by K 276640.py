# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hold_count = Counter({0: 1})
        prefix_sum = 0

        count = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]

            if prefix_sum % k in hold_count:
                count += hold_count[prefix_sum % k]
            hold_count[prefix_sum % k] += 1
        return count
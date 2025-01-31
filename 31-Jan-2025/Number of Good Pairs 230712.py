# Problem: Number of Good Pairs - https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        contain_counter = Counter()
        count = 0
        for i in range(len(nums)):
            count += contain_counter[nums[i]]
            contain_counter[nums[i]] += 1
        return count


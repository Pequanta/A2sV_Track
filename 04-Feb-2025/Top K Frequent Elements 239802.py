# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cont_counter = Counter(nums)
        res = sorted(cont_counter.keys(), key=lambda x: cont_counter[x])
        return res[-k:]
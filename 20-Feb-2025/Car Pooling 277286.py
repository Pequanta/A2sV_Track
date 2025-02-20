# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pre_sum = [0] * 1001

        for people, left , right in trips:
            pre_sum[left] += people
            pre_sum[right] -= people
        for i in range(1, len(pre_sum)):
            pre_sum[i]+= pre_sum[i - 1]
        for i in range(len(pre_sum)):
            if pre_sum[i] > capacity:
                return False

        return True
        
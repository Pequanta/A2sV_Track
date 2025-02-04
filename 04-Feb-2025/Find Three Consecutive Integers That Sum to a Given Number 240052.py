# Problem: Find Three Consecutive Integers That Sum to a Given Number - https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if (num - 3) % 3 != 0:
            return []
        first_element = (num - 3) // 3
        return [first_element, first_element + 1, first_element + 2]
# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        check = {i for i in range(left, right+1)}
        another_check = [set(range(lst[0], lst[1] + 1)) for lst in ranges]
        for i in range(len(another_check)):
            check = check.difference(another_check[i])
        return len(check) == 0
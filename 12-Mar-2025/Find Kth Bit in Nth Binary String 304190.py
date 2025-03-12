# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invertor(s):
            hold = []
            for i in range(len(s)):
                if s[i] == "1":
                    hold.append("0")
                else:
                    hold.append("1")
            return "".join(hold[::-1])
        def helper(n, k, s):
            if k <= len(s):
                return s[k - 1]
            s += "1" + invertor(s)
            return helper(n, k , s)
        return "".join(helper(n, k, "0"))
# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        forward = True
        i = 1
        while time > 0:
            if not forward and i == 1:
                forward = True
                i += 1
            elif forward and i == n:
                forward = False
                i -= 1
            elif not forward:
                i -= 1
            else:
                i += 1
            time -= 1
        return i


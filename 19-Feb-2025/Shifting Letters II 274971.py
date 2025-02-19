# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        result = [0] * (len(s) + 1)

        for shift in shifts:
            if shift[2] == 0:
                result[shift[0]] += -1
                result[shift[1] + 1] += 1
            else:
                result[shift[0]] += 1
                result[shift[1] + 1] -= 1
        for i in range(1, len(result)):
            result[i] += result[i-1]
        answer = []
        for i in range(len(s)):
            answer.append(chr((((ord(s[i]) - 97) + result[i])% 26) + 97))
        return "".join(answer)
            


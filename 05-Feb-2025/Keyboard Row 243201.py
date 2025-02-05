# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        cont_row = {0: "qwertyuiop", 1: "asdfghjkl", 2: "zxcvbnm"}

        result = []
        for word in words:
            first_row = -1
            for row in cont_row:
                if word[0].lower() in cont_row[row]:
                    first_row = row
                    break
            flag = True
            for i in range(1, len(word)):
                if word[i].lower() not in cont_row[first_row]:
                    flag = False
                    break
            if flag:
                result.append(word)
        return result

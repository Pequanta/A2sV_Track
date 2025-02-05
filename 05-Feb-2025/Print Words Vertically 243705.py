# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        cont_lst = s.split(" ")
        max_length = float("-inf")

        for word in cont_lst:
            max_length = max(max_length , len(word))
        for i in range(len(cont_lst)):
            cont_lst[i] += " " * abs(len(cont_lst[i]) - max_length)
        result = [""] * len(cont_lst[0])
        current_length = 0
        for word in cont_lst:
            for i in range(len(word)):
                if i >= len(result):
                    result.append(" " *abs(len(word)- len(result)) + word[i])
                else:
                    result[i] += word[i]
        for i in range(len(result)):
            if result[i][-1] == " ":
                while result[i][-1] == " ":
                    result[i] = result[i][:-1]
        return result
            


        
# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/


class Solution:
    def splitString(self, s: str) -> bool:
        temp_lst = []
        def check_validity(lst):
            for i in range(1, len(lst)):
                if lst[i - 1] - lst[i] != 1:
                    return False
            return True
        flag = False
        def backtracking(start_index):
            nonlocal flag
            if start_index >= len(s) and check_validity(temp_lst) and len(temp_lst) >=2:
                flag = True
                return
            if flag:
                return 
            for i in range(start_index, len(s)):
                hold = s[start_index:i + 1]
                if temp_lst and (temp_lst[-1] - int(hold) == 1):
                    temp_lst.append(int(hold))
                    backtracking(i + 1)
                    temp_lst.pop()

                elif not temp_lst:
                    temp_lst.append(int(hold))
                    backtracking(i + 1)
                    temp_lst.pop()
        backtracking(0)
        return flag
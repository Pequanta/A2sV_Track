# Problem: Sort The Students By Their Kth Score - https://leetcode.com/problems/sort-the-students-by-their-kth-score/

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(score)):
            max_index = i
            for j in range(i + 1, len(score)):
                if score[j][k] > score[max_index][k]:
                    max_index = j
            score[max_index], score[i] = score[i] , score[max_index]
        return score
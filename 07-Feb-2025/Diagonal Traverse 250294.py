# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        cont_hash = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if (i + j) in cont_hash:
                    cont_hash[i + j].append(mat[i][j])
                else:
                    cont_hash[i + j] = [mat[i][j]]
        for num in cont_hash:
            if num % 2 != 0:
                result.extend(cont_hash[num])
            else:
                result.extend(cont_hash[num][::-1])
        return result

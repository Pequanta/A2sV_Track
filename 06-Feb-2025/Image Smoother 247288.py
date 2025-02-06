# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        result = [[0] * len(img[0]) for _ in range(len(img))]
        dx_dy = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)]
        for row in range(len(img)):
            for column in range(len(img[0])):
                cont_result = img[row][column]
                count = 1
                for direction in dx_dy:
                    test = [direction[0] + row , direction[1] + column]
                    if (test[0] > -1 and test[1] > -1) and (test[0] < len(img) and test[1] < len(img[0])):
                        cont_result += img[test[0]][test[1]]
                        count += 1
                result[row][column] = cont_result // count
        return result
                



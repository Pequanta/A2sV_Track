# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        max_element = len(arr)
        result = []
        length = len(arr)
        while max_element > 0:
            index = arr.index(max_element)
            if index > 0:
                result.append(index + 1)
                temp = arr[-1 * (length - index)::-1]
                temp.extend(arr[index + 1:])
                arr = temp
            result.append(max_element)
            temp = arr[-1 * (length - max_element + 1)::-1]
            temp.extend(arr[max_element:])
            arr = temp
            max_element -= 1
        return result

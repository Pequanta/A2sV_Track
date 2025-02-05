# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_index = {list1[i]: i for i in range(len(list1)) }
        common_elements = {list2[i]: i for i in range(len(list2)) if list2[i] in list1_index}
        candidate_elements_list2 = sorted(common_elements.keys(), key=lambda x: common_elements[x])
        least_sum = -1
        for element in common_elements:
            if least_sum == -1:
                least_sum = common_elements[element] + list1_index[element]
            else:
                least_sum = min(least_sum, common_elements[element] + list1_index[element])
        result = []
        for element in common_elements:
            if common_elements[element] + list1_index[element] == least_sum:
                result.append(element)
        return result
                

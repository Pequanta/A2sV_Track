# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_counter = {}
        def get_content(file_):
            start = file_.find("(") + 1
            end =  file_.find(")")
            return [file_[start:end], file_[:start - 1]]
        result = []
        for file_ in paths:
            cont_temp = file_.split(" ")
            for i in range(1, len(cont_temp)):
                content_content = get_content(cont_temp[i])
                content = content_content[0]
                path = cont_temp[0] + "/" + content_content[1]
                if content not in content_counter:
                    content_counter[content] = [path]
                else:
                    content_counter[content].append(path)
        for path in content_counter:
            if len(content_counter[path]) > 1:
                result.append(content_counter[path])
        
        return result
            
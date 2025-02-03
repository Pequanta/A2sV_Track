# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        if len(s.split("@")) > 1:
            name, domain = s.split("@")
            domain = "".join([domain[i].lower() for i in range(len(domain))])
            name = "".join([name[i].lower() for i in range(len(name))])
            name = name[0] + ("*" * 5) + name[-1] 
            return name + "@" +  domain
        else:
            digit = list(s)
            result = ""
            count = 0
            for i in range(len(s) - 1, -1, -1):
                if s[i].isdigit():
                    if count < 4:   
                        result = s[i] + result
                    count += 1
            result = "***-***-" + result
            if count == 10:
                return result
            return "+" + "*" * (count - 10)+"-" + result



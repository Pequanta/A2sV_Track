# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num_stack = []
        for i in range(len(s)):
            if s[i].isdigit():
                if i == 0:
                    num_stack.append(s[i])
                elif s[i - 1].isdigit():
                    num_stack[-1] += s[i]
                else:
                    num_stack.append(s[i])
            else:
                if s[i] == "[":
                    stack.append("")
                elif s[i] == "]":
                    num = int(num_stack.pop())
                    word = stack.pop() * num
                    if stack:
                        stack[-1] += word
                    else:
                        stack.append(word)
                else:
                    if stack:
                        stack[-1] += s[i]
                    else:
                        stack.append(s[i])

        return "".join(stack)

                



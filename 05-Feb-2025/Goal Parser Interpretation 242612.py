# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution:
    def interpret(self, command: str) -> str:
        stack = []
        for i in range(len(command)):
            if len(stack) == 0:
                stack.append(command[i])
            elif command[i] == ")" and stack[-1] != "(":
                cont_temp = ""
                while stack[-1] != "(":
                    cont_temp = stack.pop() + cont_temp
                stack.pop()
                stack.append(cont_temp)
            elif command[i] == ")" and stack[-1] == "(":
                stack.pop()
                stack.append("o")
            else:
                stack.append(command[i])


        return "".join(stack)
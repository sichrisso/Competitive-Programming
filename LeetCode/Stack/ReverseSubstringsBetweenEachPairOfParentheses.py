def reverseParentheses(self, s: str) -> str:
        Stack = []
        result = []
        output = ""
        j = None
        for i in s:
            Stack.append(i)
            if i == ")":
                while Stack[-1] != "(":
                    if Stack[-1] ==")":
                        Stack.pop()
                    else:
                        result.append(Stack.pop())
                Stack.pop()
                Stack += result
                result = []
        return ''.join(Stack)
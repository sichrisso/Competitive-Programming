class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        for i in tokens:
            if not (i == "+" or i == "-" or i == "*" or i == "/"):
                result.append(i)
            else: 
                x=  int(result.pop())
                y=  int(result.pop())
                if (i == "+"):
                    result.append(x+y)
                elif(i == "-"):
                    result.append(y-x)
                elif(i == "*"):
                    result.append(x*y)
                else:
                    result.append(int(y/x))
        return result.pop()
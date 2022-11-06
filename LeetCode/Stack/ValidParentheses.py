def isValid(self, s: str) -> bool:
        arr = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                arr.append(i)
            else:
                if len(arr) != 0:
                    removed = arr.pop()
                    if i == ')' and removed == '(':
                        pass
                    elif i == '}' and removed == '{':
                        pass
                    elif i == ']' and removed == '[':
                        pass    
                    else:
                        arr.append(i)
                        return False
                else:
                    arr.append(i)
                    return False

        if len(arr) == 0:
            return True
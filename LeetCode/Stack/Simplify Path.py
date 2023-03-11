class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
    
        for i in range(len(path)):
            if len(path[i]) > 0 and path[i] != '.':
                if path[i] == '..' and stack:
                    stack.pop()
                    stack.pop()
                elif path[i] != '..':
                    stack.append('/')
                    stack.append(path[i])
        if not stack:
            stack.append('/')
        return "".join(stack)
       
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]  
        for char in s:
            if char == '(':
                stack.append(0)  
            else:
                last_score = stack.pop()  
                if last_score == 0: 
                    stack[-1] += 1  
                else:
                    stack[-1] += 2 * last_score 
        return stack.pop() 
            
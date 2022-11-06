def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0]*len(temperatures)
        for i in range(len(temperatures)):
            temp = temperatures[i]
            stack.append([temp,i])
            location = i
            n = len(stack) - 1
            while( i > 0 and temp > stack[n-1][0] ):
                output[stack[n-1][1]] = (location - (stack[n-1][1]))
                stack.pop(n-1)
                n -= 1
                i -= 1
        return output
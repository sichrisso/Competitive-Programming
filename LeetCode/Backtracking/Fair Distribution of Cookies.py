class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        child = [0] * k
        self.output = float('inf')
        def cookie(index, child):
            if index == len(cookies):
                unfair = max(child)
                self.output = min(self.output, unfair)
                return 
            if cookies[index] > self.output:
                return
            for childcookie in range(len(child)):
                if child[childcookie] + cookies[index] < self.output:
                    child[childcookie] += cookies[index]
                    cookie(index + 1, child)
                    child[childcookie] -= cookies[index]
        cookies.sort()
        cookie(0, child)
        return self.output



       
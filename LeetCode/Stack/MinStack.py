class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []
    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        self.minimum = self.stack.copy()
        self.minimum.sort()
        return self.minimum[0]


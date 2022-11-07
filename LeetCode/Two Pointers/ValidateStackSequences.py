def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    pointer1 = 0
    pointer2 = 0
    output = []
    while pointer2 < len(popped):
        if pointer1 == len(pushed):
            pass
        if pointer1 == len(pushed) and popped[pointer2] != pushed[pointer1-1]:
            break
        else:
            output.append(pushed[pointer1])
            pointer1 += 1
        while True:
            if len(output) > 0 and output[-1] == popped[pointer2]:
                output.pop()
                pointer2 += 1
            else:
                break
    if len(output) == 0:
        return True
    return False
def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
    tokens.sort()
    l = 0
    r = len(tokens) - 1
    score = output = 0
    while r >= l:
        if power >= tokens[l]:
            power -= tokens[l]
            score += 1
            l += 1
            output = max(output, score)
        elif score > 0:
            power += tokens[r]
            score -= 1
            r -= 1
        else:
            break
    return output
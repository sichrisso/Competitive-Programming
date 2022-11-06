def countingValleys(steps, path):
    count = 0
    valley = 0
    for i in path:
        if i == 'U':
            count += 1
            if count == 0:
                valley += 1
        else:
            count -= 1
    return valley  
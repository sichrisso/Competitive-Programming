def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    maximum = 0
    for i in range(len(trips)):
        maximum = max(maximum, trips[i][2])
    output = [0] * (maximum + 1)
    # adding the passengers when they enter and subtracting when they leave
    for i in range(len(trips)):
        output[trips[i][1]] +=  trips[i][0]
        output[trips[i][2]] += -trips[i][0]
    # summing up all the no of passengers
    prefix = 0
    for i in range(len(output)): 
        prefix += output[i]
        if prefix > capacity:
            return False
    return True
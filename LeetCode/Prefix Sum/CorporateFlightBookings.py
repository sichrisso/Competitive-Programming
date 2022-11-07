def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]: 
    output = [0] * (n+1)
    # adding the seat when they enter and subtracting when they leave
    for i in range(len(bookings)):
        output[(bookings[i][0] - 1)] +=  bookings[i][2]
        output[(bookings[i][1])] += -bookings[i][2]
    # summing up all the no of seats
    prefix = 0
    for i in range(len(output)):
        prefix += output[i]
        output[i] = prefix
    return output[:n]
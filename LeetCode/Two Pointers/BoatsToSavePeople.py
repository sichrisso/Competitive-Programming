def numRescueBoats(self, people: List[int], limit: int) -> int:
    i = 0 
    j = len(people) - 1
    output = 0
    people.sort()
    while i < j:
        if people[i] + people[j] > limit:
            output += 1
            j -= 1
        elif people[i] + people[j] <= limit:
            output += 1
            i += 1
            j -= 1
    if i == j:
        return output + 1
    return output
    
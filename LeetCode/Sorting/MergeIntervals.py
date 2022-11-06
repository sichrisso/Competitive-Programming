def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        previous = []
        while len(intervals) > 1:
            intervals.sort()
            output = []
            i = 0 
            j = 1
            if previous != intervals:
                previous = intervals
                while(i < len(intervals) and j < len(intervals)):
                    if intervals[i][0] <= intervals[j][0] <= intervals[i][1]:
                        if intervals [i][1] <= intervals[j][1]:
                            output.append([intervals[i][0], intervals[j][1]])
                        elif intervals [i][1] >= intervals[j][1]:
                            output.append([intervals[i][0], intervals[i][1]])
                        i += 2
                        j += 2
                    elif not(intervals[i][0] <= intervals[j][0] <= intervals[i][1]):
                        output.append([intervals[i][0], intervals[i][1]])
                        # output.append([intervals[j][0], intervals[j][1]])
                        i += 1
                        j += 1
                while(i < len(intervals) and len(intervals) > 1):
                     output.append([intervals[i][0], intervals[i][1]])
                     i += 1
                intervals = output

            else:
                return intervals
                break
        return intervals

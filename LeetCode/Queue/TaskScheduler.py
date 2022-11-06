def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = []
        time = 0
        output = 0
        task = Counter(tasks)
        values = sorted(task.values())
        print(values)
        while len(values) > 0:
            values.sort()
            x =  values.pop()
            x -= 1
            time += 1
            output += 1
            if x == 0:
                pass
            else: 
                queue.append([x, time + n])
            if len(values) == 0 and len(queue) > 0:
                if time != queue[0][1]:
                    diff = queue[0][1] - time
                    time += diff
                    output += diff
            elif len(values) == 0 and len(queue) == 0:
                break
            if len(queue) > 0:
                if time == queue[0][1]:  
                    y = queue.pop(0)
                    values = [y[0]] + values
        return output
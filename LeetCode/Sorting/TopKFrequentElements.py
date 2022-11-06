def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        previous = None
        output = []
        result = []
        count = 0
        nums.sort()
        for i in nums:
            if(i == previous):
                pass
            else:
                output.append([nums.count(i), i])
            previous = i
        output.sort()
        j = len(output) - 1
        while(count < k):
            result.append(output[j][1])
            count += 1
            j -= 1
        return result
                    
            
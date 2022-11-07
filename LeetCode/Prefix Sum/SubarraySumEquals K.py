def subarraySum(self, nums: List[int], k: int) -> int:
    Sum = 0
    output = 0
    dic = {}
    for i in range(len(nums)):
        if len(nums) == 1 and k != nums[i]:
            break
        Sum += nums[i]
        if Sum == k:
            output += 1
        if Sum - k in dic:
            output += dic[Sum-k]
            
        if Sum in dic:
            dic[Sum] += 1
        else:
            dic[Sum] = 1
            
        
    return output
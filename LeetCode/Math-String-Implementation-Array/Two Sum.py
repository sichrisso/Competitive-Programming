class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        dic=dict() 
        for i in range(len(nums)):
            if nums[i] in dic and i != dic[nums[i]]:
                ans.append(i)
                ans.append(dic[nums[i]])
                break
            else:
                dic[target - nums[i]] = i
        return ans
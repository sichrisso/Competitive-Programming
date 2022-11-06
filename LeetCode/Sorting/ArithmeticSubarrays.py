def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output = []
        i = 0
        j = 0
        arthimetic = True
        while(i < len(r)):
            subarray = nums[l[i]:(r[i]+1)]
            subarray.sort()
            common = subarray[j+1] - subarray[j]
            while j < len(subarray) - 1:
                if(subarray[j+1] == subarray[j] + common):
                    arthimetic = True
                else:
                    arthimetic = False
                    break
                j += 1
            if arthimetic == True:
                output.append(True)
            else:
                output.append(False)
            i += 1
            j = 0
            common = 0
        return output
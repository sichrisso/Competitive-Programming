class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n= len(numbers);
        l,r = 0,n-1;
        while(l<r):
            val = numbers[l]+numbers[r];
            if val== target:
                return [l+1,r+1];
            elif val >target:
                r-=1;
            else:
                l+=1;
        return [-1,-1];

     
from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # used montonic queue because we want to store increasing value in a queue and pop from the        beginning with o(1) operation  
        mon_que = deque()
        prefix_sum = [0]
        for i in range(len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        print(prefix_sum)

        # We want the smallest window size
        # Since negative numbers might be included and k is positive, the first num must be greater from the second for the difference to be positive numbers
        ans = len(nums) + 1
        for i in range(len(prefix_sum)):
            if len(mon_que) == 0:
                mon_que.append(i)
            else:
                # If our queue is not increasing then we will pop and arrange it  
                while mon_que and prefix_sum[i] < prefix_sum[mon_que[-1]]:
                    mon_que.pop()
                mon_que.append(i)
                # until the difference is atleast k we will shrink to search the next possible shortest subarray 
                while prefix_sum[i] - prefix_sum[mon_que[0]] >= k:
                    ans = min(ans, i-mon_que[0])
                    # If we get answer then we update our answer and remove itfrom our queue 
                    mon_que.popleft()
        #  We return the ans if we actually updated our ans if not then we return -1
        return ans if ans != len(nums) + 1 else -1
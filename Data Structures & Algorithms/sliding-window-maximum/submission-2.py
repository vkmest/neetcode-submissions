heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        curr=[(-nums[i],i) for i in range(k)]
        heapq.heapify(curr)
        res=[-(heapq.nsmallest(1,curr)[0][0])]
        for i in range(k,len(nums)):
            heapq.heappush(curr, (-nums[i],i))
            while curr[0][1]+k<=i:
                top=heapq.heappop(curr)
            res.append(-heapq.nsmallest(1,curr)[0][0])
        return res
        

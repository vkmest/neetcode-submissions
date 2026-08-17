class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_time=1
        max_time=max(piles)
        res=max_time

        while min_time<=max_time:
            mid=(min_time+max_time)//2
            times=[math.ceil(i/mid) for i in piles]
            if sum(times)<=h:
                res=min(res,mid)
                max_time=mid-1
            else:
                min_time=mid+1
        
        return res
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def area(l,r):
            return min(heights[l],heights[r])*(r-l)
        res=0
        n=len(heights)
        l,r=0,n-1
        while l<=r<n:
            cur=area(l,r)
            res=max(res,cur)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return res           
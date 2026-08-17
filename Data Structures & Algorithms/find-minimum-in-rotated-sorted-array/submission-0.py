class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        left, right = 0, n-1

        res=nums[0]

        while left<=right:
            mid=(left+right)//2

            res=min(res,nums[mid])
            if nums[mid]<=nums[right]:
                right=mid-1
                continue
            else:
                left=mid+1
        
        return res
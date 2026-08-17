class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        
        # 1. BinarySearch to find the cut point:
        left, right = 0, n-1

        res=nums[0]
        index=0
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<res:
                res=nums[mid]
                index=mid
            if nums[mid]<=nums[right]:
                right=mid-1
            else:
                left=mid+1

        # 2. BinarySearch on one of the sections
        if target<=nums[-1]:    #right section
            left, right = index, n-1
        else:   #left section
            left, right = 0, index-1

        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if target<nums[mid]:
                right=mid-1
            else:
                left=mid+1
        return -1


        return -1
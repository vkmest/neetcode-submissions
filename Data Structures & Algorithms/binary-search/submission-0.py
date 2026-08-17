class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            current=nums[m]
            if current==target:
                return m
            if current<target:
                l=m+1
                continue
            else:
                r=m-1
        return -1
            
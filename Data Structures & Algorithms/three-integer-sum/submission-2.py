class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        n=len(nums)
        for i in range(n-2):
            target=-nums[i]
            j=i+1
            k=n-1
            while j<k and j<n and k>=0:
                if nums[j]+nums[k]==target:
                    res.add((nums[i], nums[j], nums[k]))
                    j+=1
                elif nums[j]+nums[k]<target:
                    j+=1
                else: k-=1
        return list(res)
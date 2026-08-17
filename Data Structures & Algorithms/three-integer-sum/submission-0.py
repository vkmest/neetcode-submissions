class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        print(nums)
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                check=nums[j+1:]
                if (-nums[i]-nums[j]) in check:
                    res.add((nums[i],nums[j],-nums[i]-nums[j]))
                    continue
        return list(res)
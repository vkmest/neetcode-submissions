class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        dp={}
        for i in nums:
            dp[i]=1
        
        longest=0
        for i in nums:
            if i-1 in dp:
                continue
            counter=1
            num=i+1
            while num in dp:
                counter+=1
                num+=1
            longest=max(longest,counter)
        return longest

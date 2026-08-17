class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)

        table={}
        maxval=0

        for num in nums:
            prevv=table.get(num-1,0)
            nextt=table.get(num+1,0)
            
            val=prevv+nextt+1
            table[num-prevv]=val
            table[num+nextt]=val

            maxval=max(maxval,val)
        return maxval
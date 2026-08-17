class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        res=0
        cur=set()
        n=len(s)
        if n==1:
            return 1
        while l<=r<n:
            print(cur,l,r)
            while cur and s[r] in cur:
                res=max(res,len(cur))
                cur.remove(s[l])
                l+=1
            cur.add(s[r])
            r+=1
            print(cur,l,r,"----")
        res=max(res,len(cur))
        return res
            
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        abc=[0]*26
        left,right=0,0
        n=len(s)
        longest=0
        while right<n:
            abc[ord(s[right])-ord("A")]+=1
            maxi=max(abc)
            replacements=sum(abc)-maxi

            #print(left,right,replacements, abc)
            if replacements<=k:
                longest=max(longest,replacements+maxi)
            else:
                abc[ord(s[left])-ord("A")]-=1
                left+=1
            right+=1
        return longest
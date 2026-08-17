class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
    # 0. Settings:
        n,m=len(s),len(t)
        if n<m:
            return ""
        min_counter=defaultdict(int)
        mini,res=n+1,""

    # 1. Count the chars in t:
        t_counter={}
        for i in t:
            if i in t_counter:
                t_counter[i]+=1
            else: t_counter[i]=1

    # 2. Sliding window on string s:
        left, right=0,0
        can=1
        while right<n:
            if can:
                min_counter[s[right]]+=1
            print(left,right,min_counter, res, mini)
            good=1
            for i in t_counter.keys():
                if min_counter[i]<t_counter[i]:
                    good=0
                    break
            if good==0:
                right+=1
                can=1
                continue

            if (right-left+1)<mini:
                mini=right-left+1
                res=s[left:right+1]
            min_counter[s[left]]-=1
            left+=1
            can=0
    # 3. return solution
        return res    






class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n=len(temp)
        res=[0 for i in range(n)]
        stack=[]
        for i in range(n):
            cur=temp[i]
            while stack:
                last,j=stack.pop()
                if last<cur:
                    res[j]=i-j
                else: 
                    stack.append((last,j))
                    break
            stack.append((cur,i))
        return res
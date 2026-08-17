class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers=[]
        for i in tokens:
            if not (i in "+-*/"):
                numbers.append(int(i))
            else:
                second=numbers.pop()
                first=numbers.pop()
                if i=="+":    
                    res=first+second
                elif i=="-":
                    res=first-second
                elif i=="*":
                    res=first*second
                else:
                    res=abs(first)//abs(second)
                    if (first<0 and second>0) or (first>0 and second<0):
                        res=-res  
                numbers.append(res)
            print(numbers)
        return numbers[0]
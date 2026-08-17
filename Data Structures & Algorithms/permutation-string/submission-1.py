class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        counter1=[0]*26
        counter2=[0]*26

        for i in range(len(s1)):
            counter1[ord(s1[i])-ord("a")]+=1
            counter2[ord(s2[i])-ord("a")]+=1
        
        for i in range(len(s2)-len(s1)):
            if counter1==counter2:
                return True
            counter2[ord(s2[i])-ord("a")]-=1
            counter2[ord(s2[i+len(s1)])-ord("a")]+=1
        return counter1==counter2

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1={}

        for r in range(len(s1)):
            count1[s1[r]] = 1 + count1.get(s1[r], 0)

        s1_len = len(s1)

        l=0
        r= s1_len-1

        while r< len(s2):
            count2={}
            for i in range(l, r+1):
                count2[s2[i]] = 1 + count2.get(s2[i], 0)
            if count1 == count2:
                return True
            l+=1
            r+=1
        return False
                

        
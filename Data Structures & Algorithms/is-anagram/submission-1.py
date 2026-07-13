class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        
        countS = {}
        countT = {}

        for char in s:
            # countS[char] = countS.get(char, 0)  + 1
            if char in countS:
                countS[char] += 1
            else:
                countS[char] = 1
        for char in t:
            if char in countT:
                countT[char] += 1
            else:
                countT[char] = 1
        return countS == countT

        
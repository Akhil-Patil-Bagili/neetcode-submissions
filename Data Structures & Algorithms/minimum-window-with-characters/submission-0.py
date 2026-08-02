class Solution:
    def minWindow(self, s: str, t: str) -> str:

        countT={}

        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        window={}

        have, need = 0, len(countT)


        l=0
        res=[-1,-1]
        resLength= float("infinity")

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in countT and countT[c] == window[c]:
                have += 1

            while have == need:
                if (r-l+1) < resLength:
                    res=[l,r]
                    resLength = (r-l+1)
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l+=1
        l,r = res
        if resLength != float("infinity"):
            return s[l:r+1]
        else:
            return ""



        
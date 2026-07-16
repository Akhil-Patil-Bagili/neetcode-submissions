class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char for char in s if char.isalnum())
        i = 0
        j = len(cleaned)-1

        while i<=j:
            if cleaned[i].casefold() != cleaned[j].casefold():
                return False
            i+=1
            j-=1
        return True

        
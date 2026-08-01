class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            left=0
            right=len(i)-1
            while left<right:
                if i[left]!=i[right]:
                    break
                left+=1
                right-=1
            else:
                return i
        return ""

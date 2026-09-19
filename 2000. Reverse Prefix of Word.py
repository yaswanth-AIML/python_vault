class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        k=""
        l=0
        while l<len(word):
            if word[l]==ch:
                k=k+word[l]
                break
            k=k+word[l]
            l=l+1
        else:
            return word
        s=k[::-1]
        return s+word[len(s):]

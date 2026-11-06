class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        ki=[words[0]]
        for i in words:
            if sorted(ki[-1])==sorted(i):
                pass
            else:
                ki.append(i)
        return ki

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans=0
        allowed=set(allowed)
        for i in words:
            op=True
            for j in i:
                if j in allowed:
                    pass
                else:
                    op=False
                    break
            if op:
                ans+=1
        return ans

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        li={}
        ans=0
        l=0
        for r in range(len(fruits)):
            li[fruits[r]]=li.get(fruits[r],0)+1
            while len(li)>2:
                li[fruits[l]]-=1
                if li[fruits[l]]==0:
                    del li[fruits[l]]
                l+=1
            ans=max(ans,r-l+1)
        return ans

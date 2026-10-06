class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def most(k):
            count=0
            li={}
            l=0
            for i in range(len(nums)):
                li[nums[i]]=li.get(nums[i],0)+1
                while len(li)>k:
                    li[nums[l]]-=1
                    if li[nums[l]]==0:
                        del li[nums[l]]
                    l+=1
                count+=(i-l+1)
            return count
        return most(k)-most(k-1)

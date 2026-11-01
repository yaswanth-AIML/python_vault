class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums)==0:
            return []
        li=[]
        start=nums[0]
        end=None
        for i in range(len(nums)-1):
            k=nums[i]
            if k+1==nums[i+1]:
                end=nums[i+1]
            else:
                if end==None:
                    li.append(f"{start}")
                else:
                    li.append(f"{start}->{end}")
                start=nums[i+1]
                end=None
        if end==None:
            li.append(f"{start}")
        else:
            li.append(f"{start}->{end}")
        return li

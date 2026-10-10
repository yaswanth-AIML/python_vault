class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        di={}
        val=len(nums)/3
        for i in nums:
            if i in di:
                di[i]+=1
            else:
                di[i]=1
        li=[]
        for key,value in di.items():
            if value>val:
                li.append(key)
        return li

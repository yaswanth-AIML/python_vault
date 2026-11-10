class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        if len(nums)==2:
            nums.sort()
            if nums[0]==0 and nums[1]==1:
                return 2
            else:
                return 0
        li=[]
        for i in nums:
            if i==0:
                li.append(-1)
            else:
                li.append(1)
        ans=[]
        ans.append(li[0])
        for i in range(1,len(li)):
            ans.append(ans[i-1]+li[i])
        li=ans
        di={0: -1}
        maxi=0
        for i in range(len(li)):
            if li[i] in di:
                p=i-di[li[i]]
                maxi=max(maxi,p)
            else:
                di[li[i]]=i
        return maxi

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        li=[]
        less=[]
        great=[]
        for i in nums:
            if i<pivot:
                less.append(i)
            elif i==pivot:
                li.append(i)
            else:
                great.append(i)
        return less+li+great

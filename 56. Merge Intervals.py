class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        li=[]
        for i in range(len(intervals)):
            if len(li)==0 or intervals[i][0]>li[-1][1]:
                li.append(intervals[i])
            else:
                li[-1][1]=max(li[-1][1],intervals[i][1])
        return li

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max1=0
        size=len(points)
        for i in range(size):
            for j in range(i+1,size):
                for k in range(j+1,size):
                    p1=points[i]
                    p2=points[j]
                    p3=points[k]
                    area = abs(p1[0]*(p2[1]-p3[1])+p2[0]*(p3[1]-p1[1])+p3[0]*(p1[1]-p2[1]))/2
                    max1=max(max1,area)                 
        return max1

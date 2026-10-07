class Solution:
    def maxArea(self, height: List[int]) -> int:
        max1=0;left=0;right=len(height)-1
        while left<right:
            hei=min(height[left],height[right])
            wid=right-left
            max1=max(max1,wid*hei)
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        return max1

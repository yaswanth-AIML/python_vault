class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        see=set()
        right=0
        for i in range(len(nums)):
            if nums[i] in see:
                return True
            see.add(nums[i])
            if len(see)>k:
                see.remove(nums[right])
                right+=1
        else:
            return False

class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        seen=set()
        for i in range(len(arr)):
            if 2*arr[i] in seen:
                return True
            if arr[i]%2==0 and arr[i]//2 in seen:
                return True
            seen.add(arr[i])
        return False

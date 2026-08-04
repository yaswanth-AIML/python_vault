class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l=float("inf")
        result=[]     
        for i in range(len(list1)):
            if list1[i] in list2:
                j=list2.index(list1[i])
                if i+j<l:
                    l=i+j
                    result=[list1[i]]
                elif i+j==l:
                    result.append(list1[i])
        return result

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people=list(zip(heights,names))
        people.sort(reverse=True)
        rel=[]
        for height,name in people:
            rel.append(name)
        return rel

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs)<=1:
            return [strs]
        else:
            ki=[]
            visited={}
            for i in strs:
                k="".join(sorted(i))
                if k in visited:
                    visited[k].append(i)
                else:
                    visited[k]=[i]
            for i in visited.values():
                ki.append(i)
            return ki

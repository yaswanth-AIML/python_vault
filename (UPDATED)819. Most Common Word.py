class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        di={}
        k=""
        paragraph=paragraph.lower()
        paragraph = paragraph.replace(",", " ")
        paragraph = paragraph.replace(".", " ")
        paragraph = paragraph.replace("!", " ")
        paragraph = paragraph.replace("?", " ")
        paragraph = paragraph.replace(";", " ")
        paragraph=paragraph.replace("'"," ")
        words=paragraph.split()
        for i in words:
            if i in di:
                di[i]+=1
            else:
                di[i]=1
        freq=0
        ans=""
        for k,v in di.items():
            if k not in banned:
                if v>freq:
                    freq=v
                    ans=k
        return ans

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
        li=[]
        for k,v in di.items():
            li.append([v,k])
        li=sorted(li,reverse=True)
        for i in li:
            if i[1] not in banned:
                return i[1]

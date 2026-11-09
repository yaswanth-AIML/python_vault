class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        text=text.split()
        li=[]
        for i in range(len(text)-2):
            if text[i]==first and text[i+1]==second:
                li.append(text[i+2])
        return li

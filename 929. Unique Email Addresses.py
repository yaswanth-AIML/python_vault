class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        li=set()
        for word in emails:
            k=""
            at=False
            h=False
            for letter in word:
                if letter=="+" or h==True and at==False:
                    h=True
                    pass
                if letter!="@" and at==False and h==False:
                    if letter==".":
                        pass
                    else:
                        k=k+letter
                if letter=="@"or at==True:
                    at=True
                    k=k+letter
            li.add(k)
        return len(li)

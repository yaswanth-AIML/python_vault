class Solution:
    def reformatNumber(self, number: str) -> str:
        number=number.replace("-","")
        number=number.replace(" ","")
        if len(number)<=3:
            return number
        else:
            ans=""
            if len(number)==4:
                ans=f"{number[0:2]}-{number[2:4]}"
                return ans
            else:
                k=""
                for i in range(len(number)):
                    if len(k)==3:
                        if ans:
                            ans=ans+"-"+k
                        else:
                            ans=k
                        k=""
                    k=k+number[i]
                    if len(number)-i==4 and len(k)==1:
                        if ans:
                            ans=ans+"-"+number[i:i+2]+"-"+number[i+2:]
                        else:
                            ans =number[i:i+2]+"-"+number[i+2:]
                        return ans
                if ans:
                    ans=ans+"-"+k
                else:
                    ans=k
                return ans

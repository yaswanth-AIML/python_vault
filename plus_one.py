digits=[9,9,9,9,9,1,2,3,4]
for i in range(len(digits)-1,-1,-1):
    if digits[i]<9:
        digits[i]+=1
        print(digits)
        break
    digits[i]=0
    digits.insert(0,1)
    print(digits)
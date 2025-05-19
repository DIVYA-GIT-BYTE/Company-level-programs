5import math
n=int(input())
while(n!=0):
    d=n%10
    res=math.sqrt(d)
    sum+=res
    
if sum==1:
    print("Happy")
else:
    print("unhappy")


ANOTHER WAY

n=int(input())
l=[]
while True:
    sum_d=0
    for i in str(n):
        sum_d=sum_d+int(i)*int(i)
    if sum_d==1:
        print("happy")
        break
    if sum_d in l:
        print("unhappy")
        break
    else:
        l.append(sum)
    n=sum_d

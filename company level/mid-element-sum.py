l=list(map(int,input().split()))
mid,result=0,0
for i in l:
    num=str(i)
    mid=len(num)//2
    result=result+int(num[mid])
print(result)

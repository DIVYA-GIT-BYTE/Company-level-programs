l=list(map(int,input().split()))
count=0
for i in range(len(l)+1):
    for j in range(i+1,len(l)+1):
        print(l[i:j+1])
        count+=1
print(count)

l=list(map(int, input().split()))
l1=[]
max=0
count=0
for i in l[::-1]:
    if i>max:
       max=i
       count+=1
       l1.append(i)
print(l1)
print(count)
print(l1[::-1])

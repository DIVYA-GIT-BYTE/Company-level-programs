l=list(map(int,input().split()))
given_sum=int(input())
current_sum=0
l1=[]
k=0
flag=0
for i in range(len(l)):
    current_sum+=l[i]
    l1.append(l[i])
    while current_sum>given_sum:
        current_sum-=l[k]
        l1.remove(l[k])
        k+=1
    if current_sum==given_sum:
        flag=1
        print(k,i)
        print(l[k],l[i])
        print(l1[::-1])
        print(i,k)
        break

if flag==0:
    print("-1")



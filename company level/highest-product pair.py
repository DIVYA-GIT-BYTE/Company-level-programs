'''l=list(map(int,input().split()))
p=l[0]
q=l[1]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if (l[i]*l[j])>(p*q):
            p=l[i]
            q=l[j]
print(p,q)'''


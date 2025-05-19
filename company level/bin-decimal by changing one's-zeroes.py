'''n=int(input())
binary=""
sum_d=0
for i in bin(n)[2:]:
    if i=="0":
        binary=binary+"1"
    else:
        binary=binary+"0"
dv=1
for i in binary[::-1]:
    if i=='1':
        sum_d=sum_d+dv
    dv=dv*2
print(sum_d)'''
#by using range
'''for i in range(len(binary)-1,-1,-1):'''
l=list(map(int,input().split()))
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
for i in l1:
    if l.count(i)==1:
        print(i,end=' ')

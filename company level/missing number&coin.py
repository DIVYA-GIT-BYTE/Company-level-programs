'''l=list(map(int,input().split()))
n=l[-1:]
ns=n(n+1)//2
print(ns-sum(l))
'''
#normal method
'''l=list(map(int,input().split()))
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
countt=0
for i in l2:
    countt=l.count(i)
    if countt%2!=0:
        print(i,end="")
        break'''

#by using XOR operation
temp=0
l=list(map(int,input().split()))
l2=[]
for i in l:
    temp=temp^i
print(temp)

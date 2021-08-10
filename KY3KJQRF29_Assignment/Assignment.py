#l=[1,4,3,6,7,0]
#l=[-1,-3,-4,2,0,-5]

l=list(map(int,input().split()))
d={}
l1=len(l)
for i in range(l1):
    for j in range(i+1,l1):
        d[l[i]*l[j]]=[l[i],l[j]]
x=max(d.keys())
print(d[x])
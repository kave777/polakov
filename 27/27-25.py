n=int(input())
s=list(map(int,input().split()))
for _ in range(n-1):
    par=list(map(int,input().split()))
    qq=[]
    for i in s:
        for j in par:
            qq.append(i+j)
    t=[-1000]*8
    for i in qq:
        t[i%8]=max(t[i%8],i)
    s=[x for x in t if x!=-1000]
print(s[3])

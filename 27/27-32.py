n=int(input())
s=list(map(int,input().split()))
for _ in range(n-1):
    tr=list(map(int,input().split()))
    qq=[]
    for i in s:
        for j in tr:
            qq.append(i+j)
    t=[float('inf')]*11
    for i in qq:
        t[i%11]=min(t[i%11],i)
    s=[x for x in t if x!=float('inf')]
print(s[0])

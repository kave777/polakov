def get():
    a=list(map(int,input().split()))
    return list([a[1]+a[0],a[1]+a[2],a[2]+a[0]])

n=int(input())

s=get()
print(s)

for _ in range(n-1):
    tr=get()
    qq=[]
    for i in s:
        for j in tr:
            qq.append(i+j)
    t=[float('-inf')]*4
    for i in qq:
        t[i%4]=max(t[i%4],i)
    s=[x for x in t if x!=float('-inf')]
print(s)

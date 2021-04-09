def nod(a,b):
    while( a>0 and b>0):
        if a>b: a=a%b
        else: b=b%a
    return a+b
def get():
    a=list(map(int,input().split()))
    return list([nod(a[1],a[0]),nod(a[1],a[2]),nod(a[2],a[0])])

n=int(input())

s=get()
print(s)

for _ in range(n-1):
    tr=get()
    qq=[]
    for i in s:
        for j in tr:
            qq.append(i+j)
    t=[float('-inf')]*10
    for i in qq:
        t[i%10]=max(t[i%10],i)
    s=[x for x in t if x!=float('-inf')]
print(s)

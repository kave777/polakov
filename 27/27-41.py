from itertools import permutations
def get():
    a=list(map(int,input().split()))
    return list(permutations(a))

n=int(input())

s=get()
# on even - 0 0|| 0 1 || 1 1
for _ in range(n-1):
    tr=get()
    m=float('inf')
    qq=[]
    for i in s:
        for j in tr:
            qq.append([i[0]+j[0],i[1]+j[1],i[2]+j[2]])
    qq.sort(key=lambda x:x[2])
    ss=[[m,m,m]]*3
    for i in qq:
        k=i[0]%2+i[1]%2
        ss[k]=min(ss[k],i,key=lambda x:x[2])
    s=[x for x in ss if x!=[m,m,m]]
print(s[1])

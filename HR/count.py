from collections import Counter
earning=0
x=int(input())
y=list(map(int,input().split()))
n=int(input())
for i in range(n):
    a=list(map(int,input().split()))
    if a[0] in(y):
        earning+=a[1]
        y.remove(a[0])
print(earning)
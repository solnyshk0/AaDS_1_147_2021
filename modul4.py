#задача1
s=input()
stack=[]
a=0
for i in s:
    if i==")":
        if not stack or stack [-1]!="(":
            a+=1
            continue
        stack.pop()
    else:
        stack.append(i)
        

print(a+len(stack))

#задача2
from collections import deque
n=int(input())
a=deque(list(map(int, input().split(maxsplit=n))))
b=[]
deadlock=[]
res= list(range(1, n+1))
while a:
    if not deadlock or deadlock[-1] > a[0]:
        deadlock.append(a.popleft())
    if a and deadlock[-1] < a[0]:
        b.append(deadlock.pop())
    

while deadlock:
    b.append(deadlock.pop())
if b == res:
    print("YES")
else:
    print("NO")

#задача3
n=int(input())
numbers=list(map(int,input().split(maxsplit=n)))
d={i:numbers[i] for i in range(n)}
stack = []
index = [0]*n
for i in range (n-1, -1, -1):
    while stack and stack[-1][1]>=d[i]:
        stack.pop()
    if not stack:
        index[i]= -1
    else:
        index[i]=stack[-1][0]
    stack.append([i,d[i]])

print(*index)



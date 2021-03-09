#задача5
k={}
n=int(input())
x=input()
array=x.split()
for i in arr:
    k[int(i)]=1
print(len(k))

#задача6
a=int(input())
b=list(map(int,input().split()))
z=int(input())
ord=list(map(int,input().split()))
count=[0]*(a+1)
for now in ord:
    count[now]+=1
for i in range(sklad):
    if b[i]<count[i+1]:
        print ('yes')
    else:
        print ('no')

n1,n2=map(int,input().split())
count=0
li=[]
for i in range (1,n1+1):
    li.append(i)
for i in li:
    print(i,end=" ")
for li in range(0,n2+1):
    count=count+li
print(count)
   

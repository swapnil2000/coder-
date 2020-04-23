a=[]
n=int(input('Enter the Rnage  '))
for i in range(1,n+1):
    s=0
    t1=t2=i
    count=0
    while t1>0:
        count=count+1
        t1=t1//10
    while t2>0:
        r=t2%10
        s=s+r**count
        t2=t2//10
    if i==s:
        a.append(i)
print('Armstrong numbers in a list')
print(a)

m1=int(input('Enter the first no.   '))
m2=int(input('Enter the second no.  '))
d=0
for n in range(m1,m2):
    s=0
    t1=t2=n
    c=0
    while n>0:
        c=c+1
        n=n//10
    while t1>0:
        r=t1%10
        s=s+r**c
        t1=t1//10
    if t2==s:
        print(t2)
        d=d+1
print('Total no. of armstong   ',d)

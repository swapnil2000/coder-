p=[]

n=int(input('Entre the  Range  '))

for i in range(2,n+1):

    f=1

    for j in range(2,i):

        if i%j==0:

           f=0

           break

    if f==1:

        p.append(i)

print(p)

n=int(input('Entre the size of the MATRIX:    '))
magicsquare=[[0 for i in range(n)]for j in range(n)]
print('Start of matrix',magicsquare)
i=n//2
j=n-1
num=1
if n%2==1:
    while num<=(n*n):
        if i==-1 and j==n:#3rd condition 
            j=n-2
            j=0
        else:
            if j==n:
                j=0
            if i<0:
                i=n-1
        if magicsquare[int(i)][int(j)]:#2nd condition
            j=j-2
            i=i+1
            continue
        else:
            magicsquare[int(i)][int(j)]=num
            num=num+1
        j=j+1
        i=i-1#1st condition
    #print condition in matrix form 
    print('Magic Square for n= ',n)
    print('Sum of each row or column',n*(n*n+1)//2,"\n")
    for i in range(0,n):
        for j in range(0,n):
            print('%2d'%(magicsquare[i][j]),end="   ")
            if j==n-1:
                print()
else:
    print('Entre an ODD NUMBER')
    


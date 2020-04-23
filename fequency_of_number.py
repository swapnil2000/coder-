l = list(map(int,input("Enter no. to check frequency spliting by space = ").split()))
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
for i in l2:
    print("The frequency of {} is {}".format( i,l.count(i)))

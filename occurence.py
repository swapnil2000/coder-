s=input('Entre the String= ')
l2=[]
for i in s:
    if i not in l2:
        l2.append(i)
for i in l2:
    print(i,' is occuring ',s.count(i),' times')
    

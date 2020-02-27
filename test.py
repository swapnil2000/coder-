l=['red','white','black','red','green','black']
l.sort()
print(l)
s=[]
for i in l:
    if i not in s:
        s.append(i)
print(s)

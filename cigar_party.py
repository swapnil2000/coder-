a=input()
x=a.split(',')
x1=int(x[0])
x2=x[1]
if x2=='True'and x1>=40:
        print("True")
elif x1>=40 and x1<=60:
        print("True")
else:
        print("False")
        

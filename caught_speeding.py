a=input()
x=a.split(',')
x1=int(x[0])
x2=x[1]
if x2=='False':
        if x1<=60:
                print('0')
        elif x1>=61 and x1<=80:
                print('1')
        else:
                print('2')
else:
        if x1<=65:
                print('0')
        elif x1>=66 and x1<=85:
                print('1')
        else:
                print('2')

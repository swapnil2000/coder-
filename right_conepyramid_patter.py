x=1
n=int (input())
for i in range(1,2*n):
        for j in range(1,n+1):
                if i<=n:
                        if i>=j:
                            print('*',end='')
                else:
                        print((2*n-i)*'*',end='')
                        break
                
        
                  
            
        print()
            
                

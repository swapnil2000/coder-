t=int(input())
for i in range(1,t+1):
    a,b=map(str, input().split())
    try:
        print(int(a)/int(b))
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as f:
        print("Error Code:",f)

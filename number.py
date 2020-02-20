n=input('Entre the phone number= ')
if len(n)==10:
    if n.isdigit():
        if n.count("0")==10:
            print('Not Valid')
        else:
            print('Valid')
        if n.startswith('9'):
            print('Valid')
        else:
            print('Not valid')
    else:
        print("Not Valid")
else:
    print("Not Valid")

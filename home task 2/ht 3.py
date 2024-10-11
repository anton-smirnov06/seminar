a = input()
b=reg=False
for i in range(0,len(a)):
    if a[i]=='3':
        a=a.replace('3','E')
        b=True
    elif a[i]=='L':
        a=a.replace('L','J')
        b=True
    elif a[i]=='2':
        a=a.replace('2','S')
        b=True
    elif a[i]=='5':
        a=a.replace('5','Z')
        b=True
    elif a[i] not in ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8']:
        reg=True
w=a[::-1]
if w==a:
    if reg and b:
        print(a, 'is a mirrored string.')
    if not reg:
        print(a, 'is a mirrored palindrome.')
    if reg and not b:
        print(a, 'is a regular palindrome.')
else:
    print(a, 'is not a palindrome.')

    

    
    
    
        
    

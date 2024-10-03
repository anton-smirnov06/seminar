a,b = map(int,input().split(' '))
a1 = a
b1 = b
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
d = a + b
x = 0
while True:
    y = (d - a1*x)/b1
    if y == int(y):
        print(x,int(y),d)
        break
    y = (d - a1*(-x))/b1
    if y == int(y):
        print(-x,int(y),d)
        break
    x = x + 1

    

x = list(map(int,input().split(' ')))
y = list(map(int,input().split(' ')))
a = 0
for i in range(len(x)):
    a = a + x[i]*y[i]
a = a/len(x)
q = 0
for i in range(len(x)):
    q = q + x[i]*x[i]
q = q/len(x)
xx = sum(x)/len(x)
yy = sum (y)/len(y)
k = (a - xx*yy)/(q - xx**2)
b = yy - k*xx
print(k)
print(b)

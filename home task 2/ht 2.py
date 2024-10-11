g, a = input().split()
b = ''
g = int(g)
for i in range (0, len(a), g):
    b = b + a[i:i+g][::-1]    
print(b)

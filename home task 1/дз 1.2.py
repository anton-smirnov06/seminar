n = int(input())
ans = list()
for i in range(2, int(n ** 0.5) + 1):
    while n % i == 0:
        n = n // i
        ans.append(i)
if n != 1: ans.append(n)
print(*ans)        
        
        
    
    

"""x = 10
while x:
    x = x - 1
    if x % 2 != 0: 
        continue 
    print(x, end=' ')
else: 
    print("Finally decreased to ZERO")
    
print('............................')

y = 20
while y:
    y = y - 1
    if y % 2 != 0: 
        continue 
    print(y, end=' ')
else: 
    print("Finally decreased to ZERO")
"""
import math
n = 0
x = 1
z = 4
while abs(x - n) > math.exp(-10):
    n = x
    x = (n+(z/x))/2
    print(x)

    break

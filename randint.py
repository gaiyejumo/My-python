from random import randint

"""x = randint(1,10)
y = "Faith"
for i in range(x):
    print(y)
print('Random integer is {}'.format(x))

"""



# x = int(input('Input a number for x: '))
# y = int(input('Input a number for y: '))
"""
def num(x, y):
    z = abs(x-y)
    c = x+y
    n = z/c
    return z

print(num(x,y))

#      OR

z = abs(x-y)
c = x + y
n = z / c

print(n)
"""

# Write a program that asks the user to enter an angle between −180◦ and 180◦. Using an expression with the modulo operator, convert the angle to its equivalent between 0◦ and 360◦.

x = int(input('Input a value: '))
if 0 == x or x <= 180:
    print(x)
elif x == 180:
    print(x)
elif x >= -180 or x <= -90:
    print(180 - x)
elif x >= -90 or x <= 0:
    print(270 - x)
else:
    print('Input a valued number')


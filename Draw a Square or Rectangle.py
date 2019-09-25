x = int(input("Input a value to specify how wide: "))
z = int(input("Input a value to specify how high: "))
# y = str(input("What's your name? "))
for i in range(1):
    print('*'*(x) + ('\n*' + ' '*(x-2) + '*')*(z))
    print('*'*(x))

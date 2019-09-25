def fib(f):
    if f <= 1:
        return f
    else:
        return ((fib(f-1)) + (fib(f-2)))

n = eval(input('Determine the length of the terms: '))
if n <= 0:
    print('Please provide positive integers only')
else:
    for i in range(n):
        print(fib(i), end=' ')

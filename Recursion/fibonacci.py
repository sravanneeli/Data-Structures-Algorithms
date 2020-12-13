n = 10
f = [-1 for _ in range(n)]

def fib(n):
    global f
    if n <= 1:
        f[n] = n
        return n
    else:
        if (f[n-2] == -1):
            f[n-2] = fib(n-2)
        if f[n-1] == -1:
            f[n-1] = fib(n-1)
        return f[n-2] + f[n-1]

def main():
    print("{} term of fibonacci series is : {}".format(n ,fib(n)))


main()
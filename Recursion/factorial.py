def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n

def main():
    n = 15
    factn = factorial(n)
    print("Factorial of {} is {}".format(n, factn))

if __name__ == "__main__":
    main()
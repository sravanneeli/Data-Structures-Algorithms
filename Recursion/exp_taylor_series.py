p = 1.0
f = 1.0
def exp(x, n):
    global p, f
    if n == 0:
        return 1
    r = exp(x, n-1)
    p = p * x
    f = f * n
    return r + (p / f)


def main():
    x = 3
    n = 10 # till ho wmany terms exponentail should be approximated
    print("Exponential of {} with {} terms is: {}".format(x, n ,exp(x, n)))


main()
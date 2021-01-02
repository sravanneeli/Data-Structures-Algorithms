s = 1.0

def exp_horner(x, n):
    global s
    if n == 0:
        return s
    s = 1 + (x/n) * s
    return exp_horner(x, n-1)

def main():
    x = 3
    n = 10 # till ho wmany terms exponentail should be approximated
    print("Exponential of {} with {} terms is: {}".format(x, n ,exp_horner(x, n)))

if __name__ == "__main__":
    main()
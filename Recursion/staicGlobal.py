x = 0

def func(n):
    global x
    if n == 0:
        return 0
    if n > 0:
        x += 1
        return func(n-1) + x


def main():
    r = func(5)
    print(r)

if __name__ == "__main__":
    main()
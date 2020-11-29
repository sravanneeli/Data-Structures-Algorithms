def func(n):
    if n == 0:
        return 1
    if n > 0:
        print(n)
        func(n-1)
        func(n-1)

def main():
    func(3)

if __name__ == "__main__":
    main()
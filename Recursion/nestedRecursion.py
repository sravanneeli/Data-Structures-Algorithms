def func(n):
    if n > 100:
        return n - 10
    return func(func(n+11))


def main():
    result = func(95)
    print(result)

if __name__ == "__main__":
    main()
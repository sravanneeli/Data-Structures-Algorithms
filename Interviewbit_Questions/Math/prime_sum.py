def sieve(n):
    prime = [True] * (n + 1)
    prime[0] = False
    p = 2

    while p * p <= n:

        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    return prime


def prime_sum(n):
    prime = sieve(n)
    for i in range(2, n + 1):
        if prime[i] and prime[n-i]:
            return [i, n-i]


def main():
    n = 15000
    print(f"Even number represented as two prime numbers is : {prime_sum(n)}")


if __name__ == '__main__':
    main()

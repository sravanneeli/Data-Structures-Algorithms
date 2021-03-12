def SquareRoot(x):
    start = 0
    end = x//2
    ans = 1
    if x == 1:
        return 1
    while start <= end:
        mid = (start + end) // 2
        if mid * mid == x:
            return mid
        if mid * mid < x:
            start = mid+1
            ans = mid
        else:
            end = mid-1
    return ans

def main():
    x = 200
    print(f"Square root of {x} is: {SquareRoot(x)}")

if __name__ == '__main__':
    main()
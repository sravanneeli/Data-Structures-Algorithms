# using swapping
def permutate_string(a, l, h, res):
    if l == h:
        res.append("".join(a))
    else:
        for i in range(l, h):
            a[i], a[l] = a[l], a[i]
            permutate_string(a, l+1, h, res)
            a[l], a[i] = a[i], a[l]


# with auxilary bits array
def permutate(a, l, r, res, bits, temp):    
    if l == r:
        res.append("".join(temp))
    else:
        for i in range(len(a)):
            if bits[i] == 0:
                temp[l] = a[i]
                bits[i] = 1
                permutate(a, l+1, r, res, bits, temp)
                bits[i] = 0
    
    

def main():
    a = 'abcd'
    temp = [char for char in a]
    bits = [0] * len(a)
    res = []
    permutate(a, 0, len(a), res, bits, temp)
    print(res)
    res = []
    temp = [char for char in a]
    permutate_string(temp, 0, len(a), res)
    print(res)
    



if __name__ == "__main__":
    main()
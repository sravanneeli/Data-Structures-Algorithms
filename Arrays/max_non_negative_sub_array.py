# Maximum continous non negative sub array #  
def max_non_negative(A):
    i, j = 0, 0
    n = len(A)
    sum_dict = {}
    sub_sum = 0
    while i < n and j < n:
        if A[j] >= 0:
            sub_sum += A[j]
            j += 1
        else:
            sum_dict[(i, j)] = sub_sum
            j += 1
            i = j
            sub_sum = 0
    
    sum_dict[(i, j)] = sub_sum
    max_sum = max(sum_dict.values())
    max_len = -99999999
    max_sum_arr = []

    for key in sum_dict:
        if max_sum == sum_dict[key]:
            max_sum_arr.append(key)

    start, end=0, 0
    for key in max_sum_arr:
        if (key[1] - key[0]) > max_len:
            max_len = key[1] - key[0]
            start, end = key[0], key[1]

    return A[start:end]
        


def main():
    A = [ 0, 0, -1, 0 ]
    print(max_non_negative(A))


def coverPoints(A, B):
    steps = 0
    for i in range(1,len(A)):
        steps += max(abs(A[i]-A[i-1]),abs(B[i]-B[i-1]))
    return steps

def main():
    A = [0, 1, 4]
    B = [0, 1, 4]
    print("Minimum steps to cover the start point to end point:",coverPoints(A, B))


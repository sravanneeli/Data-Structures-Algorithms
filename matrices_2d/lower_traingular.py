# row major method
class Matrix:
    def __init__(self, A=[], n=None):
        self.A = A
        self.n = n

def set_value(m, i, j, x):
    if (i >= j):
        m.A[i*(i-1)//2+j-1] = x

def display(m):
    for i in range(1, m.n+1):
        for j in range(1, m.n+1):
            if i >= j:
                print(m.A[i*(i-1)//2+j-1], end = ' ')
            else:
                print(0, end=' ')
        print()
    
def main():
    m = Matrix()
    m.n = int(input("Enter Dimention for the matrix: "))
    m.A = [0] * ((m.n * (m.n + 1))//2)
    print("Enter all Elements: ")
    for i in range(1, m.n+1):
        for j in range(1, m.n+1):
            x = int(input())
            set_value(m, i, j, x)
    display(m)
    

if __name__ == "__main__":
    main()
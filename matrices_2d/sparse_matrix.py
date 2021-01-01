class Element:
    def __init__(self, i=0, j=0, x=0):
        self.i = i
        self.j = j
        self.x = x

class Sparse:
    def __init__(self, m=0, n=0, num=0):
        self.m = m
        self.n = n
        self.num = num
        self.ele = []

def create(s):
    s.m, s.n = map(int, input("Enter Dimensions: ").split())
    s.num = int(input("Enter Number of Non zero elements: "))
    print("Enter Non Zero Elements")
    for _ in range(s.num):
        temp_i, temp_j, temp_x = map(int, input().split())
        s.ele.append(Element(temp_i, temp_j, temp_x))
    return s
    

    
def display(s):
    k = 0
    for i in range(s.m):
        for j in range(s.n):
            if (i == s.ele[k].i) and (j == s.ele[k].j) and k < len(s.ele):
                print(s.ele[k].x, end=' ')
                k += 1
            else:
                print(0, end=' ')
        print()

def main():
    s = Sparse()
    s = create(s)
    display(s)

if __name__ == "__main__":
    main()


    
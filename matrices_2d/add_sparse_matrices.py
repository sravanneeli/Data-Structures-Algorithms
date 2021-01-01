from sparse_matrix import *

def add_sparse(s1, s2):
    if s1.m == s2.m and s1.n == s2.n:
        c = Sparse()
        c.m, c.n = s1.m, s1.n
        i = j = k = 0
        while i < s1.num and j < s2.num:
            if s1.ele[i].i < s2.ele[j].i:
                temp_i, temp_j, temp_x = s1.ele[i].i, s1.ele[i].j, s1.ele[i].x
                c.ele.append(Element(temp_i, temp_j, temp_x))
                i += 1
            elif s1.ele[i].i > s2.ele[j].i:
                temp_i, temp_j, temp_x = s2.ele[j].i, s2.ele[j].j, s2.ele[j].x
                c.ele.append(Element(temp_i, temp_j, temp_x))
                j += 1
            else:
                if s1.ele[i].j < s2.ele[j].j:
                    temp_i, temp_j, temp_x = s1.ele[i].i, s1.ele[i].j, s1.ele[i].x
                    c.ele.append(Element(temp_i, temp_j, temp_x))
                    i += 1
                elif s1.ele[i].j > s2.ele[j].j:
                    temp_i, temp_j, temp_x = s2.ele[j].i, s2.ele[j].j, s2.ele[j].x
                    c.ele.append(Element(temp_i, temp_j, temp_x))
                    i += 1
                else:
                    temp_i, temp_j, temp_x = s1.ele[i].i, s1.ele[i].j,  \
                                                    s1.ele[i].x + s2.ele[j].x

                    c.ele.append(Element(temp_i, temp_j, temp_x))
                    i += 1; j += 1

        for k in range(i, s1.num):
            c.ele.append(Element(s1.ele[k].i, s1.ele[k].j, s1.ele[k].x))
        
        for k in range(j, s2.num):
            c.ele.append(Element(s2.ele[k].i, s2.ele[k].j, s2.ele[k].x))
        return c

    else:
        return "Dimensions of matrices doesn't match."

# Given non zero values should be row wise and sorted
def main():
    s1 = Sparse()
    s1 = create(s1)
    s2 = Sparse()
    s2 = create(s2)
    c = add_sparse(s1, s2) # c = s1 + s2
    print("Sum of two sparse matrix is: ")
    display(c)



if __name__ == "__main__":
    main()
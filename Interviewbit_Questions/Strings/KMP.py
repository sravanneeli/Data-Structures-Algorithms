def kmp(pat, txt):
    m = len(txt)
    n = len(pat)
    lps = compute_lps(pat)
    i, j = 0, 0
    while i < m:
        if pat[j] == txt[i]:
            i += 1 
            j += 1
        if j == n:
            print ("Found pattern at index " + str(i-j))
            j = lps[j-1]
        elif i < m and pat[j] != txt[i]:
            if j != 0 :
                j= lps[j-1]
            else:
                 i += 1
    
        

def compute_lps(pat):
    n = len(pat)
    lps = [0] * n
    i = 1
    le = 0
    while i < n :
        if pat[i] == pat[le]:
            le += 1
            lps[i] = le
            i += 1
        else:
            if le != 0:
                le = lps[le-1]
            else:
                lps[i] = 0
                i += 1

    return lps


def main():
    pat = "abbabbbbbccabaabaaabbb"
    kmp('abb', pat)

if __name__ == '__main__':
    main()
    
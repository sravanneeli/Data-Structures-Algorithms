"""
Validate if a given string is numeric.

Examples:

"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

"""

def isnumber(num):
    num = num.strip()
    n = len(num)
    if n == 0:
        return 0

    if num[0] == '+' or num[0] == '-':
        num = num[1:]
        n = n - 1
        if n == 0:
            return 0
    i = 0
    dotencountered = False
    eentocuntered = False

    while i < n:
        if num[i] >= '0' and num[i] <= '9':
            i += 1
            continue
        
        if num[i] == '.':
            if dotencountered:
                return 0
            dotencountered = True
            i += 1

            if i >= n:
                return 0
            elif num[i] == 'e':
                return 0
            
        elif num[i] == 'e':
            if eentocuntered:
                return 0
            eentocuntered = True
            dotencountered = True
            i += 1
            if i < n and (num[i] == '-' or num[i] == '+'):
                i += 1
        else:
            return 0
    return 1


def main():
    a = '2e10'
    print(isnumber(a))

if __name__ == '__main__':
    main()
    

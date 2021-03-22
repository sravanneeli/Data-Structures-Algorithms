"""
Problem Description

Given a string A consisting only of lowercase characters, we need to check whether it is possible to make this string a palindrome after removing exactly one character from this.

If it is possible then return 1 else return 0.
"""


def convert_to_palindrome(pat):
    n = len(pat)
    
    if pat == pat[::-1]:
        return True

    i, j = 0, n-1

    while i < n and j >= 0:
        if pat[i] == pat[j]:
            i += 1
            j -= 1
        else:
            break
    
    temp1 = pat[:i] + pat[i+1:]
    if temp1 == temp1[::-1]:
        return True

    temp2 = pat[:j] + pat[j+1:]
    if temp2 == temp2[::-1]:
        return True
        
    return False


def main():
    pat = "abecebad"
    print(f"convert to plaindrome possible or not: {convert_to_palindrome(pat)}")     


if __name__ == '__main__':
    main()
    
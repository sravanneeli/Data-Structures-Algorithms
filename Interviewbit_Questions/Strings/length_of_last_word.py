"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Given s = "Hello World",

return 5 as length("World") = 5.

Please make sure you try to solve this problem without using library functions. Make sure you only traverse the string once.
"""


def length_of_last_word(pat):
    i = len(pat) - 1

    while i >= 0 and pat[i] == " ":
        i -= 1

    last = i

    if last == -1:
        return 0

    while i > 0 and pat[i-1] != " ":
        i -= 1
    
    return last - i + 1


def main():
    pat = "Hello World          "
    print(f"Last word length: {length_of_last_word(pat)}")

if __name__ == '__main__':
    main()
    

    
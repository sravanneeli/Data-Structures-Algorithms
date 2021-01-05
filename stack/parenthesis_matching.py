"""
    Parenthesis Matching: whether braces are matching in a string
"""
from stack.stack_class import Stack


def is_balanced(exp):
    st = Stack(len(exp))
    st.create()
    for i in range(len(exp)):
        if exp[i] == '(':
            st.push(exp[i])
        elif exp[i] == ')':
            if st.is_empty():
                return False
            st.pop()
    return st.is_empty()


def main():
    exp = '((a+b)*(c-d))'
    print("The expression parenthesis are balanced or not ?", is_balanced(exp))


if __name__ == '__main__':
    main()

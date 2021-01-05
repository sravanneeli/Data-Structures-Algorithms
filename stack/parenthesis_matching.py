"""
    Parenthesis Matching: whether braces are matching in a string
"""
from stack.stack_class import Stack

bracket_dict = {')': '(', ']': '[', '}': '{'}


def is_balanced(exp):
    """
    Check whether all the parenthesis are balanced are not
    :param exp: expression in string format
    :return: True or False
    """
    st = Stack(len(exp))
    st.create()
    for i in range(len(exp)):
        if exp[i] == '(' or exp[i] == '[' or exp[i] == '{':
            st.push(exp[i])
        elif exp[i] == ')' or exp[i] == ']' or exp[i] == '}':
            if st.is_empty():
                return False
            x = st.pop()
            if bracket_dict[exp[i]] != x:
                return False
    return st.is_empty()


def main():
    exp = '({a+b}*(c-d))'
    print("The expression parenthesis are balanced or not ?", is_balanced(exp))


if __name__ == '__main__':
    main()

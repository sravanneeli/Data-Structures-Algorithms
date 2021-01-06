from stack.stack_class import Stack


class Conversion:
    def __init__(self, infix):
        self.size = len(infix)
        self.infix = infix
        self.st = Stack(self.size)
        self.postfix = ""
        self.prefix = ""
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def infix_to_postfix(self):
        i = 0
        self.st.create()
        while i < self.size:
            # print(i)
            if self.is_operand(self.infix[i]):
                self.postfix += self.infix[i]
                i += 1
            else:
                if self.is_precedent(self.infix[i]) or self.st.is_empty():
                    self.st.push(self.infix[i])
                    i += 1
                else:
                    self.postfix += self.st.pop()
        while not self.st.is_empty():
            self.postfix += self.st.pop()
        return self.postfix

    @staticmethod
    def is_operand(ch):
        return ch.isalpha()

    def is_precedent(self, ch):
        try:
            a = self.precedence[ch]
            b = self.precedence[self.st.top_ele()]
            return True if a > b else False

        except KeyError:
            return False


def main():
    infix = 'a+b*c+d-e*f+g*h-i'
    convert = Conversion(infix)
    postfix = convert.infix_to_postfix()
    print("Infix to Postfix expression:", postfix)


if __name__ == '__main__':
    main()

class Conversion:

    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def isEmpty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.array[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    def push(self, op):
        self.top += 1
        self.array.append(op)

    def isOperand(self, ch):
        return ch.isalnum()

    def notGreaterThan(self, operator):
        try:
            operatorPrecedence = self.precedence[operator]
            stackPrecedence = self.precedence[self.peek()]
            return True if operatorPrecedence <= stackPrecedence else False
        except KeyError:
            return False

    def infixToPostfix(self, exp):
        for i in exp:
            if self.isOperand(i):
                self.output.append(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                while (not self.isEmpty()) and self.peek() != '(':
                    a = self.pop()
                    self.output.append(a)
                if not self.isEmpty() and self.peek() != '(':
                    return -1
                else:
                    self.pop()
            else:
                while not self.isEmpty() and self.notGreaterThan(i):
                    self.output.append(self.pop())
                self.push(i)
        while not self.isEmpty():
            self.output.append(self.pop())

        print("".join(self.output))

    def prefixToInfix(self, expr):
        for i in reversed(expr):
            if self.isOperand(i):
                self.push(i)
            else:
                firstOperand = self.pop()
                secondOperand = self.pop()
                finalString = "(" + firstOperand + i + secondOperand + ")"
                self.push(finalString)
        print(self.pop())

    def prefixToPostFIx(self,expr):
        for i in reversed(expr):
            if self.isOperand(i):
                self.push(i)
            else:
                firstOperand = self.pop()
                secondOperand = self.pop()
                finalString = firstOperand+secondOperand+i
                self.push(finalString)
        print(self.pop())

    def postfixToPreFix(self,expr):
        for i in expr:
            if self.isOperand(i):
                self.push(i)
            else:
                firstOperand = self.pop()
                secondOperand = self.pop()
                finalString = i+secondOperand+firstOperand
                self.push(finalString)
        print(self.pop())

    def postfixToInfix(self,expr):
        for i in expr:
            if self.isOperand(i):
                self.push(i)
            else:
                firstOperand = self.pop()
                secondOperand = self.pop()
                finalString = "("+secondOperand+i+firstOperand+")"
                self.push(finalString)
        print(self.pop())

expr = "(d+c)*b+a"
conv = Conversion(len(expr))
conv.infixToPostfix(expr)

expr1 = "*-A/BC-/AKL"
conv1 = Conversion(len(expr1))
conv.prefixToInfix(expr1)

expr2 = "*-A/BC-/AKL"
conv2 = Conversion(len(expr2))
conv2.prefixToPostFIx(expr2)

expr3 = "ABC/-AK/L-*"
conv3 = Conversion(len(expr3))
conv3.postfixToPreFix(expr3)

expr4 = "ab*c+"
conv4 = Conversion(len(expr4))
conv4.postfixToInfix(expr4)

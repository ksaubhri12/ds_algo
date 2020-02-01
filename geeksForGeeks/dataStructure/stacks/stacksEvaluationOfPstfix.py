def postfixEvaluation(expr):
    numberStack = []
    numbers = expr.split(" ")
    for i in numbers:
        if i.isalnum():
            numberStack.append(float(i))
        else:
            firstOperand = numberStack.pop()
            secondOperand = numberStack.pop()
            if i == "*":
                finalNumber = secondOperand * firstOperand
            elif i == "+":
                finalNumber = secondOperand + firstOperand
            elif i == "-":
                finalNumber = secondOperand - firstOperand
            elif i == "/":
                finalNumber = secondOperand / firstOperand
            else:
                finalNumber = pow(secondOperand, firstOperand)
            numberStack.append(finalNumber)
    print(numberStack.pop())

expr = "100 200 + 2 / 5 * 7 +"
postfixEvaluation(expr)

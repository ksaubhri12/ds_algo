def printNGE(arr):
    numberStacks = []
    numberStacks.append(arr[0])

    i = 1
    while i < len(arr):
        next = arr[i]

        if len(numberStacks):
            topElement = numberStacks.pop()
            while topElement < next:
                print(str(topElement)+"--- "+str(next))
                if not len(numberStacks):
                    break
                topElement = numberStacks.pop()
            if topElement > next:
                numberStacks.append(topElement)
        numberStacks.append(next)
        i = i+1
    while  len(numberStacks):
        print(str(numberStacks[-1])+"--- "+"-1")
        numberStacks.pop()

printNGE([35,30,10,5,50,60,70])







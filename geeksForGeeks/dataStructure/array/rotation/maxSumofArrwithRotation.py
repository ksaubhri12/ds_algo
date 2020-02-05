def calculateMaxSum(arr):
    arraySum = sum(arr)
    n = len(arr)
    calculatedValue = 0
    for i in range(n):
        calculatedValue += i * arr[i]
    maxValue = calculatedValue
    for i in range(1, n):
        calculatedValue = calculatedValue + arraySum - n * arr[n - i]
        if calculatedValue > maxValue:
            maxValue = calculatedValue
    print(maxValue)


arr = [1, 20, 2, 10]
calculateMaxSum(arr)

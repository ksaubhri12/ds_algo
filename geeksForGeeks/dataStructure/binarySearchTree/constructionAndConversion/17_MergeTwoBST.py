class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def mergeTwoBST(root1, root2):
    arr1 = []
    arr2 = []
    inOrderTraversalUtil(root1,arr1)
    inOrderTraversalUtil(root2,arr2)
    arr3 = merge(arr1,arr2)
    root = createBalanceBSTFromSortedArray(arr3)
    return root



def merge(leftArray, rightArray):
    leftArrayIndex = 0
    rightArrayIndex = 0
    finalArray = [None] * (len(leftArray) + len(rightArray))
    finalArrayIndex = 0

    while leftArrayIndex < len(leftArray) and rightArrayIndex < len(rightArray) and finalArrayIndex < len(
            leftArray) + len(rightArray):
        if leftArray[leftArrayIndex] <= rightArray[rightArrayIndex]:
            finalArray[finalArrayIndex] = leftArray[leftArrayIndex]
            leftArrayIndex += 1
        else:
            finalArray[finalArrayIndex] = rightArray[rightArrayIndex]
            rightArrayIndex += 1
        finalArrayIndex += 1
    if finalArrayIndex == len(leftArray) + len(rightArray):
        return finalArray
    if leftArrayIndex == len(leftArray):
        for value in rightArray[rightArrayIndex:]:
            finalArray[finalArrayIndex] = value
            finalArrayIndex += 1
        return finalArray
    if rightArrayIndex == len(rightArray):
        for value in leftArray[leftArrayIndex:]:
            finalArray[finalArrayIndex] = value
            finalArrayIndex += 1
        return finalArray

def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.data)
        printInOrder(root.right)

def inOrderTraversalUtil(root, arr):
    if root:
        inOrderTraversalUtil(root.left, arr)
        arr.append(root.data)
        inOrderTraversalUtil(root.right, arr)

def createBalanceBSTFromSortedArray(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        root = Node(arr[0])
        return root
    high = len(arr) - 1
    low = 0
    mid = high + (low - high) / 2
    mid = int(mid)
    root = Node(arr[mid])
    root.left = createBalanceBSTFromSortedArray(arr[:mid])
    root.right = createBalanceBSTFromSortedArray(arr[mid+1:])
    return root


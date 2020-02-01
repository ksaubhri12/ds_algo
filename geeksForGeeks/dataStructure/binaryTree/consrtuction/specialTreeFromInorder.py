class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

    def constructSpecialTreeFromInorder(self,arr):
        if len(arr) == 1:
            return Node(arr[0])
        if len(arr) == 0:
            return None
        maxValue, maxIndex = Node.maxValueAndIndexInArr(arr)
        temp = Node(maxValue)
        temp.left = self.constructSpecialTreeFromInorder(arr[:maxIndex])
        temp.right = self.constructSpecialTreeFromInorder(arr[maxIndex+1:])

        return temp


    def printInorder(self, root):
        if root:
            self.printInorder(root.left)
            print(root.data)
            self.printInorder(root.right)

    @staticmethod
    def maxValueAndIndexInArr(arr):
        if len(arr):
            maxValue = arr[0]
            maxIndex = 0

            for i in range(len(arr)):
                if arr[i]>maxValue:
                    maxValue = arr[i]
                    maxIndex = i
            return maxValue,maxIndex

arr = [5, 10, 40, 30, 28]
node = Node()
root = node.constructSpecialTreeFromInorder(arr)
node.printInorder(root)

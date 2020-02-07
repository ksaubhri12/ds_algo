class BSTNode:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


# def constructTree(pre):
#     size = len(pre)
#     constructTreeUtil.preIndex = 0
#     return constructTreeUtil(pre, 0, size - 1, size)
#
#
# def constructTreeUtil(pre, low, high, size):
#     if getPreIndex() >= size or low > high:
#         return None
#     root = BSTNode(pre[getPreIndex()])
#     incrementPreIndex()
#     if low == high:
#         return root
#     i = 0
#     for i in range(low, high + 1):
#         if pre[i] > root.data:
#             break
#     root.left = constructTreeUtil(pre, getPreIndex(), i - 1, size)
#     root.right = constructTreeUtil(pre, i, high, size)
#     return root


def incrementPreIndex():
    constructTreeUtil.preIndex += 1


def getPreIndex():
    return constructTreeUtil.preIndex


def preInorder(root):
    if root:
        preInorder(root.left)
        print(root.data)
        preInorder(root.right)


INT_MIN = float("-infinity")
INT_MAX = float("infinity")


def constructTree(pre):
    size = len(pre)
    constructTreeUtil.preIndex = 0
    key = pre[0]
    return constructTreeUtil(pre,key,INT_MIN,INT_MAX,size)


def constructTreeUtil(pre, key, min, max, size):
    if getPreIndex() >= size:
        return None
    root = None
    if key > min and key < max:
        root = BSTNode(key)
        incrementPreIndex()
        if getPreIndex() < size:
            root.left = constructTreeUtil(pre,pre[getPreIndex()],min,key,size)
            root.right = constructTreeUtil(pre,pre[getPreIndex()],key,max,size)

    return root



root = constructTree([10, 5, 1, 7, 40, 50])
preInorder(root)

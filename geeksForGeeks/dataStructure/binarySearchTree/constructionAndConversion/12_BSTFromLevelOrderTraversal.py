# class Node:
#
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# def constructBSTFromLevelOrderTraversalArray(arr):
#     n = len(arr)
#     root = constructBSTUtil(arr, n, 0)
#     return root
#
#
# def constructBSTUtil(arr, n, i):
#     if i < n:
#         root = Node(arr[i])
#         root.left = constructBSTUtil(arr, n, 2 * i + 1)
#         root.right = constructBSTUtil(arr, n, 2 * i + 2)
#         return root
#     return None
#
#
# def printInorder(root):
#     if root:
#         printInorder(root.left)
#         print(root.data)
#         printInorder(root.right)
#
# arr = [7, 4, 12, 3, 6, 8, 1, 5, 10]
# root = constructBSTFromLevelOrderTraversalArray(arr)
# printInorder(root)
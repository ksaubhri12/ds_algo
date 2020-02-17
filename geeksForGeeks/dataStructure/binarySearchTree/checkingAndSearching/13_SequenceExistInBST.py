class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isSequenceExistInBST(root, seq):
    i = [0]
    isSeqExistUtil(root, seq, i)
    if i[0] == len(seq) :
        return True
    else:
        return False


def insert(root, key):
    if root is None:
        return Node(key)
    if root.data > key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def isSeqExistUtil(root, seq, i):
    if root:
        isSeqExistUtil(root.left, seq, i)
        if root.data == seq[i[0]]:
            i[0] += 1
        isSeqExistUtil(root.right, seq, i)

root = None
seq = [4, 6, 8, 14]
root = insert(root, 8)
root = insert(root, 10)
root = insert(root, 3)
root = insert(root, 6)
root = insert(root, 1)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 14)
root = insert(root, 13)
print(isSequenceExistInBST(root,seq))


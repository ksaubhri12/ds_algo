class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None



def isBSTContainSameElement(root1,root2):
    set1 = set()
    set2 = set()
    storeSet(root1,set1)
    storeSet(root2,set2)
    if len(set2) != len(set1):
        return False
    return set1 == set2


def storeSet(root,set):
    if root:
        storeSet(root.left,set)
        set.add(root.data)
        storeSet(root.right,set)
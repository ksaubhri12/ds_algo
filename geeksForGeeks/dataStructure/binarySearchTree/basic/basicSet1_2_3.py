class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, root, key):
        if root is None:
            return -1
        if root.data == key:
            return root
        if key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def insert(self, root, key):
        if root is None:
            root = BSTNode(key)
            return root
        if root.left is None and key < root.data:
            root.left = BSTNode(key)
            return root
        if root.right is None and key > root.data:
            root.right = BSTNode(key)
            return root
        if key < root.data:
            self.insert(root.left, key)
        else:
            self.insert(root.right, key)
        return root

    def inorderPrint(self, root):
        if root:
            self.inorderPrint(root.left)
            print(root.data)
            self.inorderPrint(root.right)

    def minValueNode(self, root):
        curr = root
        while curr.left is not None:
            curr = curr.left
        return curr

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.data:
            root.left = self.delete(root.left, key)
        if key > root.data:
            root.right = self.delete(root.right, key)
        if key == root.data:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.minValueNode(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        return root


r = BSTNode(50)
r.insert(r, 30)
r.insert(r, 20)
r.insert(r, 40)
r.insert(r, 70)
r.insert(r, 60)
r.insert(r, 80)
r.delete(r, 20)
# r.inorderPrint(r)
r.delete(r, 30)
r.delete(r, 40)
r.delete(r, 60)
r.inorderPrint(r)

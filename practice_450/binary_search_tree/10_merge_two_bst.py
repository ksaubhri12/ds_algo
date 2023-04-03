class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right


def merge_bst(root1: TreeNode, root2: TreeNode):
    ll_1 = [None]
    head_l1 = [None]
    in_order_util(root1, ll_1, head_l1)
    ll_2 = [None]
    head_l2 = [None]
    in_order_util(root2, ll_2, head_l2)
    merged_dll = merge_two_dll(head_l1[0], head_l2[0])
    return merged_dll


def in_order_util(root: TreeNode, prev: [], head: []):
    if root is None:
        return
    in_order_util(root.left, prev, head)
    if head[0] is None:
        head[0] = root
        prev[0] = root
    else:
        prev[0].right = root
        root.left = prev[0]
        prev[0] = root
    in_order_util(root.right, prev, head)


def merge_two_dll(ll_1: TreeNode, ll_2: TreeNode):
    if ll_1 is None:
        return ll_2
    if ll_2 is None:
        return ll_1

    if ll_1.data < ll_2.data:
        val = merge_two_dll(ll_1.right, ll_2)
        ll_1.right = val
        val.left = ll_1
        return ll_1

    else:
        val = merge_two_dll(ll_1, ll_2.right)
        ll_2.right = val
        val.left = ll_2
        return ll_2


if __name__ == '__main__':
    node_1 = TreeNode(24)
    node_2 = TreeNode(18)
    node_3 = TreeNode(11)
    node_4 = TreeNode(10)
    node_5 = TreeNode(5)

    node_1.left = node_2
    node_2.left = node_3
    node_3.left = node_4
    node_4.left = node_5

    anode_1 = TreeNode(8)
    anode_2 = TreeNode(2)
    anode_3 = TreeNode(18)
    anode_4 = TreeNode(1)
    anode_5 = TreeNode(22)
    anode_1.left = anode_2
    anode_1.right = anode_3

    anode_2.left = anode_4
    anode_3.right = anode_5

    merge_bst(node_1, anode_1)

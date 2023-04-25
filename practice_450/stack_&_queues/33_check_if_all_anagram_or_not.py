from practice_450.binary_tree import Node


def check_anagram(tree_1: Node, tree_2: Node):
    level_map = {}
    queue_1 = [tree_1]
    queue_2 = [tree_2]

    while len(queue_1) > 0 and len(queue_2) > 0:

        n1 = len(queue_1)
        n2 = len(queue_2)

        if n1 != n2:
            return False

        if n1 == 0:
            return False

        if n2 == 0:
            return False

        for i in range(n1):
            element_pop = queue_1.pop(0)
            if element_pop.data in level_map:
                level_map[element_pop.data] = level_map[element_pop.data] + 1
            else:
                level_map[element_pop.data] = 1

            if element_pop.left is not None:
                queue_1.append(element_pop.left)
            if element_pop.right is not None:
                queue_1.append(element_pop.right)

        for i in range(n2):
            element_pop = queue_2.pop(0)
            if element_pop.data not in level_map:
                return False

            level_map[element_pop.data] = level_map[element_pop.data] - 1
            if level_map[element_pop.data] == 0:
                del level_map[element_pop.data]

            if element_pop.left is not None:
                queue_2.append(element_pop.left)
            if element_pop.right is not None:
                queue_2.append(element_pop.right)

        if len(level_map) != 0:
            return False
    if len(queue_1) != 0 or len(queue_2) != 0:
        return False

    return True


if __name__ == '__main__':
    node_1 = Node.Node(1)
    node_2 = Node.Node(3)
    node_3 = Node.Node(2)

    node_1.left = node_2
    node_1.right = node_3

    anode_1 = Node.Node(1)
    anode_2 = Node.Node(2)
    anode_3 = Node.Node(3)

    anode_1.left = anode_2
    anode_1.right = anode_3

    print(check_anagram(node_1, anode_1))

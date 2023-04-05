from Node import Node
from typing import List


class Solution:

    def findLeastGreater(self, n: int, arr: List[int]) -> List[int]:
        return self.replace_element_least_greater(arr)

    def replace_element_least_greater(self, input_arr: []):
        n = len(input_arr)
        head_node = [None]
        for i in reversed(range(0, n)):
            succ_node = [None]
            self.add_node_return_successor(head_node, head_node[0], input_arr[i], succ_node)
            if succ_node[0] is None:
                input_arr[i] = -1
            else:
                input_arr[i] = succ_node[0]

        return input_arr

    def add_node_return_successor(self, head_node: [], curr_node: Node, data, success_node: []):

        if head_node[0] is None:
            head_node[0] = Node(data)
            curr_node = Node(data)
            return curr_node

        if curr_node is None:
            return Node(data)

        if data < curr_node.data:
            success_node[0] = curr_node.data
            curr_node.left = self.add_node_return_successor(head_node, curr_node.left, data, success_node)
        else:
            curr_node.right = self.add_node_return_successor(head_node, curr_node.right, data, success_node)

        return curr_node


if __name__ == '__main__':
    print(Solution().findLeastGreater(15, [8, 58, 71, 18, 31, 32, 63, 92,
                                           43, 3, 91, 93, 25, 80, 28]))

from Node import Node
from LinkedList import LinkedList


class Solution:

    def mergeSort(self, head: Node):
        if head is None:
            return None

        if head.next is None:
            return head
        split_linked_list_heads = self.split_give_two_linked_list(head)
        left_sorted_linked_list = self.mergeSort(split_linked_list_heads[0])
        right_sorted_linked_list = self.mergeSort(split_linked_list_heads[1])
        return self.merge_sorted_linked_list(left_sorted_linked_list, right_sorted_linked_list)

    def merge_sorted_linked_list(self, head_1: Node, head_2: Node):
        if head_1.data <= head_2.data:
            new_head = Node(head_1.data)
            curr_head_1 = head_1.next
            curr_head_2 = head_2

        else:
            new_head = Node(head_2.data)
            curr_head_1 = head_1
            curr_head_2 = head_2.next

        curr = new_head

        while curr_head_1 is not None or curr_head_2 is not None:

            if curr_head_1 is None:
                curr.next = Node(curr_head_2.data)
                curr_head_2 = curr_head_2.next

            elif curr_head_2 is None:
                curr.next = Node(curr_head_1.data)
                curr_head_1 = curr_head_1.next

            elif curr_head_1.data <= curr_head_2.data:
                curr.next = Node(curr_head_1.data)
                curr_head_1 = curr_head_1.next

            else:
                curr.next = Node(curr_head_2.data)
                curr_head_2 = curr_head_2.next

            curr = curr.next

        return new_head

    def get_count(self, head: Node):
        count = 0
        curr = head
        while curr is not None:
            count = count + 1
            curr = curr.next

        return count

    def split_give_two_linked_list(self, head: Node):
        count = self.get_count(head)

        if count % 2 == 0:
            half_count = count // 2 - 1
        else:
            half_count = count // 2

        curr = head
        while half_count > 0:
            curr = curr.next
            half_count = half_count - 1

        if curr is not None:
            new_head = curr.next
            curr.next = None
        else:
            new_head = None
        return [head, new_head]


if __name__ == '__main__':
    sol = Solution()

    node_1 = Node(3)
    node_2 = Node(6)
    node_3 = Node(9)
    node_4 = Node(15)
    node_5 = Node(30)
    node_6 = Node(40)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6

    mnode_1 = Node(10)
    mnode_2 = Node(12)
    mnode_3 = Node(14)
    mnode_4 = Node(15)
    mnode_5 = Node(18)
    mnode_6 = Node(34)
    mnode_1.next = mnode_2
    mnode_2.next = mnode_3
    mnode_3.next = mnode_4
    mnode_4.next = mnode_5
    mnode_5.next = mnode_6
    ll_1 = LinkedList(node_1)
    print('Linked List 1')
    ll_1.print_linked_list()
    ll_2 = LinkedList(mnode_1)
    print('Linked List 2')
    ll_2.print_linked_list()
    new_node = sol.merge_sorted_linked_list(node_1, mnode_1)
    ll_3 = LinkedList(new_node)
    print('Sorted Linked List')
    ll_3.print_linked_list()
    print('Splitting linked list 1 into equal linked list')
    new_two_nodes = sol.split_give_two_linked_list(node_1)
    ll_4 = LinkedList(new_two_nodes[0])
    ll_5 = LinkedList(new_two_nodes[1])
    ll_4.print_linked_list()
    ll_5.print_linked_list()

    node_1 = Node(3)
    node_2 = Node(5)
    node_3 = Node(2)
    node_4 = Node(4)
    node_5 = Node(1)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    ll_6 = LinkedList(node_1)
    print('Unsorted Linked List')
    ll_6.print_linked_list()
    print('Perform Sorting')
    new_node = sol.mergeSort(node_1)
    print('Sorted Linked List')
    ll_7 = LinkedList(new_node)
    ll_7.print_linked_list()

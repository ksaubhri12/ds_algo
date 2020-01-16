from geeksForGeeks.dataStructure.linkedList import LinkedList,Node

#
# li = LinkedList()
# li.append(15)
# li.append(10)
# li.append(5)
# li.append(22)
# li.append(21)
# li.append(37)
# li.append(63)
# li.append(22)
#
#
# li.printLinkedList(li.head)
# sortedHead = li.mergeSort(li.head)
# print("sorted linked list is")
# li.printLinkedList(sortedHead)

# node1 = Node(1)
# node2 = Node(2)
# node1.next = node2
# node2.next = Node(3)
# node2.next.next = Node(4)
# node2.next.next.next = Node(5)
# node2.next.next.next.next = node2
#
#
# LinkedList.detectAndCountLoop(node1)

li = LinkedList()
li.append(10)
li.append(15)
li.append(12)
li.append(13)
li.append(20)
li.append(14)

newHead = LinkedList.swapNodes(li.head,12,20)
LinkedList.printLinkedList(newHead)





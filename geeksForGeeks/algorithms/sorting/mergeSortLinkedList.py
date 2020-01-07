from geeksForGeeks.dataStructure.linkedList import LinkedList


li = LinkedList()
li.append(15)
li.append(10)
li.append(5)
li.append(22)
li.append(21)
li.append(37)
li.append(63)
li.append(22)


li.printLinkedList(li.head)
sortedHead = li.mergeSort(li.head)
print("sorted linked list is")
li.printLinkedList(sortedHead)






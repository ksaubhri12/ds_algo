# Absolute path to simple/canonical path
#
# "/home/d/../b/c////..f"
# ANS - "/home/b/c/..f"


# Home , d, .. , b , c, ..f
#
# New_head_node =
# Curr_node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_path(str_value: str):
    split_arr = str_value.split('/')
    new_head_node = None
    curr_node = None
    prev_node = None
    for i in range(0, len(split_arr)):
        element = split_arr[i]

        if element != '.' and element != '..' and element != '':
            if new_head_node is None:
                new_head_node = Node(element)
                curr_node = new_head_node
                prev_node = None

            else:
                prev_node = curr_node
                curr_node.next = Node(element)
                curr_node = curr_node.next

        elif element == '..':
            if prev_node is not None:
                prev_node.next = None
                curr_node = prev_node

        else:
            continue

    final_string = ''
    curr = new_head_node
    while curr is not None:
        final_string = final_string + '/' + str(curr.data)
        curr = curr.next

    return final_string


if __name__ == '__main__':
    print(create_path('/home/d/../b/c/../e/..f'))
    print(create_path('/home/d/../b/c////..f'))
    print(create_path('//..//../asd..'))
    print(create_path('/home//foo/'))
    print(create_path('/a/./'))

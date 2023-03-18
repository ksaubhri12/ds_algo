# Given a string
# return smallest string possible by replacing the characters with $ symbol that repeat from the beginning of the string
# input -> kkalpesh
# output -> k$alpesh
# input ->  aabcdaabcdfg
# output -> a$bcd$fg
#           aabcdaabcdfg


#           aabcdzabcdfg
#           a$
#           a$bcdz$fg
        #   aabcdzaabcdzfg
#           a bcd a abcdfg
#
#           a$bcdaabcdfg -> replace



# Given two BST you have to find out the nodes that exist only in one of the  two trees in terms of values
#               20                                      13
#          10          30                       8                20
#       9      11   25     31             7           11      17      25
#
#       9                  31
#   7                  25
#
#


class BST:
    def __init__(self):
        self.value = None
        self.right = None
        self.left = None


def get_non_common_element_in_bst(bst1: BST, bst2: BST):
    return










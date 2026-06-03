"""
The trick is to calculate the number of boss
if the number of boss is X, you would need X-1 extra edges
Total number of min  edges you need for a connected graph is V-1
if my total edges > V-1 + X -1, then I can borrow some edges and connect the graph
"""


class DisjointSet:

    def __init__(self, n):
        self.rank_array = [0] * (n + 1)
        self.parent_array = [i for i in range(n + 1)]

    def ultimate_parent(self, node):
        parent_node = self.parent_array[node]
        if parent_node == node:
            return node

        self.parent_array[node] = self.ultimate_parent(parent_node)
        return self.parent_array[node]

    def union_by_rank(self, u, v):
        parent_u = self.ultimate_parent(u)
        parent_v = self.ultimate_parent(v)

        if parent_u == parent_v:
            return

        if self.rank_array[parent_u] == self.rank_array[parent_v]:
            self.parent_array[parent_v] = parent_u
            self.rank_array[parent_u] += 1
        elif self.rank_array[parent_u] > self.rank_array[parent_v]:
            self.parent_array[parent_v] = parent_u
        else:
            self.parent_array[parent_u] = parent_v


def number_of_operation(V, edges):
    ds = DisjointSet(V)
    for edge in edges:
        ds.union_by_rank(edge[0], edge[1])

    bosses = 0
    for i in range(V):
        if ds.parent_array[i] == i:
            bosses += 1

    min_edges = bosses - 1
    if min_edges == 0:
        return 0

    total_edges = len(edges)
    if total_edges - (V - 1) >= 0:
        return min_edges
    else:
        return -1


if __name__ == '__main__':
    print(number_of_operation(4, [[0, 1], [0, 2], [1, 2]]))
    print(number_of_operation(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]))

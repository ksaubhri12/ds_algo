"""
Used for graph, dynamic graphs, that keeps on changing

main function -> parent, union by rank, union by size
"""


class NormalDisjointSet:

    def __init__(self, V):
        self.parent_array = [i for i in range(V + 1)]

    def ultimate_parent(self, node):
        if self.parent_array[node] == node:
            return node

        self.parent_array[node] = self.ultimate_parent(
            self.parent_array[node]
        )

        return self.parent_array[node]

    def union(self, x, z):
        parent_x = self.ultimate_parent(x)
        parent_z = self.ultimate_parent(z)

        if parent_x != parent_z:
            self.parent_array[parent_x] = parent_z


def handle_queries(n, queries):
    ds = NormalDisjointSet(n)

    answer_arr = []

    for query in queries:

        if query[0] == 1:
            ds.union(query[1], query[2])

        else:
            answer_arr.append(
                ds.ultimate_parent(query[1])
            )

    return answer_arr


class DisjointSetSize:
    def __init__(self, n):
        self.size_arr = [1] * (n + 1)
        self.parent_array = [i for i in range(n + 1)]

    def ultimate_parent(self, node):
        if self.parent_array[node] == node:
            return node

        self.parent_array[node] = self.ultimate_parent(
            self.parent_array[node]
        )

        return self.parent_array[node]

    def union_by_size(self, from_node, to_node):
        parent_from_node = self.ultimate_parent(from_node)
        parent_to_node = self.ultimate_parent(to_node)

        if self.size_arr[parent_from_node] >= self.size_arr[parent_to_node]:
            self.parent_array[parent_to_node] = parent_from_node
            self.size_arr[parent_from_node] += self.size_arr[parent_to_node]
        else:
            self.parent_array[parent_from_node] = parent_to_node
            self.size_arr[parent_to_node] += self.size_arr[parent_from_node]


class DisjointSet:

    def __init__(self, V):
        self.rank_array = [0] * (V + 1)
        self.parent_array = [i for i in range(V + 1)]

    def ultimate_parent(self, node):
        parent_node = self.parent_array[node]
        if node == parent_node:
            return node
        self.parent_array[node] = self.ultimate_parent(parent_node)
        return self.parent_array[node]

    def union_by_rank(self, from_node, to_node):
        parent_from_node = self.ultimate_parent(from_node)
        parent_to_node = self.ultimate_parent(to_node)

        if parent_from_node == parent_to_node:
            return

        if self.rank_array[parent_from_node] == self.rank_array[parent_to_node]:
            self.rank_array[parent_from_node] += 1
            self.parent_array[parent_to_node] = parent_from_node
        elif self.rank_array[parent_from_node] > self.rank_array[parent_to_node]:
            self.parent_array[parent_to_node] = parent_from_node
        else:
            self.parent_array[parent_from_node] = parent_to_node


if __name__ == '__main__':
    print(handle_queries(5, [[2, 4], [2, 1], [1, 3, 1], [2, 3]]))
    print(handle_queries(6, [[1, 2, 3], [1, 4, 5], [2, 2], [2, 3], [1, 3, 5], [2, 4]]))

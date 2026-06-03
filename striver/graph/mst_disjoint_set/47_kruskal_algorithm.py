"""
Sort all the edges according to the weight
"""


class DisjointSet:

    def __init__(self, n):
        self.rank_array = [0 for i in range(n + 1)]
        self.parent_array = [i for i in range(n + 1)]
        self.weight = 0
        self.mst_arr = []

    def ultimate_parent(self, node):
        if self.parent_array[node] == node:
            return node

        self.parent_array[node] = self.ultimate_parent(
            self.parent_array[node]
        )

        return self.parent_array[node]

    def union_by_rank(self, u, v, w):
        parent_u = self.ultimate_parent(u)
        parent_v = self.ultimate_parent(v)
        if parent_u == parent_v:
            return

        self.weight += w
        if self.rank_array[parent_u] == self.rank_array[parent_v]:
            self.parent_array[parent_v] = parent_u
            self.rank_array[parent_u] += 1
        elif self.rank_array[parent_u] > self.rank_array[parent_v]:
            self.parent_array[parent_v] = parent_u
        else:
            self.parent_array[parent_u] = parent_v


def sorted_edges(edges):
    new_edges = sorted(edges, key=lambda x: x[2])
    return new_edges


def kruskal_algorithm(n, edges):
    ds = DisjointSet(n)
    edges = sorted_edges(edges)
    for edge in edges:
        ds.union_by_rank(edge[0], edge[1], edge[2])
    return ds.weight


if __name__ == '__main__':
    print(kruskal_algorithm(3, [[0, 1, 5], [1, 2, 3], [0, 2, 1]]))
    print(kruskal_algorithm(2, [[0, 1, 5]]))
    print(kruskal_algorithm(4, [[0, 1, 6], [0, 2, 3], [1, 3, 9], [0, 3, 1], [2, 3, 6]]))
    print(kruskal_algorithm(7, [[0, 1, 3],[1, 3, 3],[1, 5, 10],[2, 4, 6],[2, 6, 9],[3, 6, 8],[4, 5, 6]]))

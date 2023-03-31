from Graph import Graph


def check_graph_tree(graph: Graph):
    visited = [False] * graph.V

    if is_cyclic(graph, 0, visited, -1):
        return False

    for i in range(0, graph.V):
        if not visited[i]:
            return False

    return True


def is_cyclic(graph: Graph, v, visited, parent):
    visited[v] = True

    for i in graph.graph[v]:
        if not visited[i]:
            if is_cyclic(graph, i, visited, v):
                return True

        elif i != parent:
            return True

    return False

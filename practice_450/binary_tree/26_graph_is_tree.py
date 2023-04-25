# We need to check two things
# If the whole graph can be traverse by a single point which is our root - possibility of tree
# Apart from that if there is no cyclic relation - It is definitely a tree
# The recursive function take two things.
# One is node and second one is parent of the node.
# when we visit a node - mark it as visited,
# run the same code for all other adjacent neighbour of that node. There if any node you find which is visited and that

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

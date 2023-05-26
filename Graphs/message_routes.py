def search_and_mark(vertex, edges):
    # Initialize tracking arrays
    node_count = len(edges)
    parents = [-1] * node_count
    visited = [False] * node_count
    # Initialize the open list
    open_list = [vertex]
    # Breadth first search through the nodes marking the parent tree
    while len(open_list) > 0:
        curr = open_list.pop(0)
        for target in edges[curr]:
            if not visited[target]:
                visited[target] = True
                parents[target] = curr
                open_list.append(target)
    # Done with search return parent tree
    return parents

def message_routes(computers, connections):
    # Build graph as adjacency list
    edges = [[] for _ in range(computers)]

    # Add connections as edges
        # NOTE: vertices are 0 based but computers are 1 based
    for connection in connections:
        # connections are bidirectional
        edges[connection[0] - 1].append(connection[1] - 1)
        edges[connection[1] - 1].append(connection[0] - 1)
    parents = search_and_mark(1, edges)
    # Couldn't find the end computer
    # Path not possible
    if parents[computers - 1] == -1:
        return None
    # Build the path
    path = []
    curr = computers - 1
    while curr != 0:
        path.insert(0, curr + 1)
        curr = parents[curr]
    path.insert(0, 1)
    return path


def main():
    computers = 5
    connections = [
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 3],
        [5, 4]
    ]
    print(message_routes(computers, connections))

main()
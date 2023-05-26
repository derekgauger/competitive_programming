def dfs(curr, tgt, edges, visited):
    # Skip the node if it has already been visited
    if visited[curr]:
        return False
    # If the target was found, then a path exists
    if curr == tgt:
        return True
    # Mark the node visited and continue searching all targets
    visited[curr] = True
    for target in edges[curr]:
        if dfs(target, tgt, edges, visited):
            return True
    return False

def find_a_path_dfs(src, tgt, V, E):
    # Build a graph as adjacency list
    visited = [False for _ in range(V)]
    edges = []
    for i in range(V):
        edges.append([])
        visited[i] = False
    # NOTE: Vertices are 1 based but arrays are 0 based
    for e in E:
        edges[e[0] - 1].append(e[1] - 1)
    return dfs(src - 1, tgt - 1, edges, visited)

def find_a_path_bfs(src, tgt, V, E):
    # Build graph as adjacency list
    visited = [False for _ in range(V)]
    edges = []
    for i in range(V):
        edges.append([])
        visited[i] = False
    # NOTE: Vertices are 1 based but arrays are 0 based
    for e in E:
        edges[e[0] - 1].append(e[1] - 1)
    # Intialize the open list to the source node
    open_list = []
    open_list.append(src - 1)

    # Search for the target
    while len(open_list) > 0:
        curr = open_list.pop(0)
        # Skip the node if it has already been visited
        if visited[curr]:
            continue
        # If the target was found, then a path exists
        if curr == tgt - 1:
            return True
        # Mark the node visited and continue searching all targets
        visited[curr] = True
        for target in edges[curr]:
            open_list.append(target)
    return False

def main():
    vertices = 6
    edges = [
        [1, 2],
        [1, 5],
        [2, 3],
        [2, 5],
        [3, 4],
        [4, 5],
        [4, 6]
    ]
    print(find_a_path_bfs(1, 6, vertices, edges))
    print(find_a_path_dfs(1, 6, vertices, edges))

main()
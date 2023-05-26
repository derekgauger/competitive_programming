EVEN = 0
ODD = 1

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

def find_a_path_dfs(src, tgt, even_odd, V, E):
    # Build a graph as adjacency list
    visited = [False for _ in range(V*2)]
    edges = []
    for i in range(V*2):
        edges.append([])
        visited[i] = False
    # NOTE: vertices are 1 based but arrays are 0 based
    # Connect even to odd vertices
    # Connect odd to even vertices
    for e in E:
        src_even = e[0] - 1
        src_odd = e[0] + V - 1
        tgt_even = e[1] - 1
        tgt_odd = e[1] + V - 1
        edges[src_even].append(tgt_odd)
        edges[src_odd].append(tgt_even)

    tgt_even = tgt - 1
    tgt_odd = tgt + V - 1
    if even_odd == ODD:
        real_target = tgt_odd
    else:
        real_target = tgt_even
    return dfs(src - 1, real_target, edges, visited)

def find_a_path_bfs(src, tgt, even_odd, V, E):
    # Build graph as adjacency list
    visited = [False for _ in range(V*2)]
    edges = []
    for i in range(V*2):
        edges.append([])
        visited[i] = False
    # NOTE: vertices are 1 based but arrays are 0 based
    # Connect even to odd vertices
    # Connect odd to even vertices
    for e in E:
        src_even = e[0] - 1
        src_odd = e[0] + V - 1
        tgt_even = e[1] - 1
        tgt_odd = e[1] + V - 1
        edges[src_even].append(tgt_odd)
        edges[src_odd].append(tgt_even)
    # Intialize the open list to the source node
    open_list = []
    open_list.append(src - 1)
    tgt_even = tgt - 1
    tgt_odd = tgt + V - 1
    if even_odd == ODD:
        real_target = tgt_odd
    else:
        real_target = tgt_even
    # Search for the target
    while len(open_list) > 0:
        curr = open_list.pop(0)
        # Skip the node if it has already been visited
        if visited[curr]:
            continue
        # If the target was found, then a path exists
        if curr == real_target:
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
    print(find_a_path_bfs(1, 6, ODD, vertices, edges))
    print(find_a_path_dfs(1, 6, EVEN, vertices, edges))

main()
def build_teams(students, friendships):
    # Build graph as adjacency list
    edges = [[] for _ in range(students)]
    visited = [False for _ in range(students)]
    groups = [0 for _ in range(students)]

    for i in range(students):
        edges.append([])
        visited[i] = False
        groups[i] = 0
    
    # Add relationships as edges
    # NOTE: Vertices are 0 based but friendships are 1 based
    for friendship in friendships:
        # Friendships are bidirectional
        edges[friendship[0] - 1].append(friendship[1] - 1)
        edges[friendship[1] - 1].append(friendship[0] - 1)

    for i in range(students):
        if not visited[i]:
            open_list = []
            open_list.append(i)
            groups[i] = 1

            while len(open_list) > 0:
                curr = open_list.pop(0)
                for target in edges[curr]:
                    if groups[target] == groups[curr]:
                        return None
                    if not visited[target]:
                        visited[target] = True
                        if groups[curr] == 1:
                            groups[target] = 2
                        else:
                            groups[target] = 1
                        open_list.append(target)

    return groups

def main():
    students = 5
    relationships = [
        [1, 2],
        [1, 3],
        [4, 5],
    ]
    print(build_teams(students, relationships))

main()
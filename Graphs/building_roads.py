def search_and_mark(vertex, visited, edges):
    # Mark the vertex as visited
    visited[vertex] = True
    # Search for neighbor vertices
    for neighbor in edges[vertex]:
        if not visited[neighbor]:
            search_and_mark(neighbor, visited, edges)
    
def build_roads(cities, roads):
    # Build graph as adjacency list
    edges = [[] for _ in range(cities)]
    visited = [False] * cities
    # Add roads as edges
    # NOTE: vertices are 0 based but cities are 1 based
    for road in roads:
        # Roads are bidirectional
        edges[road[0] - 1].append(road[1] - 1)
        edges[road[1] - 1].append(road[0] - 1)
    
    # Find all the connected components
    components = []
    for i in range(cities):
        if not visited[i]:
            components.append(i)
            search_and_mark(i, visited, edges)

    # All cities connected, then no roads are needed
    if len(components) == 1:
        return None
    
    # Some roads need to be built, return the array of roads to connect the components
    #     NOTE edges are 0 based but cities are 1 based
    new_roads = [[0 for _ in range(len(components) - 1)] for _ in range(2)]
    for i in range(len(components) - 1):
        new_roads = [components[i] + 1, components[i + 1] + 1]
    return new_roads

def main():
    cities = 4
    roads = [
        [1, 2],
        [3, 4]
    ]
    print(build_roads(cities, roads))

main()
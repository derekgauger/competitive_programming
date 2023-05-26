def course_schedule(course_count, prereqs):
    course_order = [0] * course_count
    # Build graph as adjacency list
    edge_count = [0] * course_count
    edges = [[] for _ in range(course_count)]
    # Add prereqs as edges
    for prereq in prereqs:
        edges[prereq[1]].append(prereq[0])
        # Record the edge count to later use to add nodes to the openlist
        edge_count[prereq[0]] += 1
    
    # Search for topological ordering
    # Initialize the open list to all vertices
    # with no incoming edges
    open_list = []
    for i in range(course_count):
        if edge_count[i] == 0:
            open_list.append(i)
    
    # Search
    # Pull off a course from the open list
    # Add it to the schedule
    # Remove the edges from that course to children (e.g., reduce the degree)
    # Add courses to the open list with no incoming edges
    course_order_length = 0
    while len(open_list) > 0:
        course = open_list.pop(0)
        course_order[course_order_length] = course
        course_order_length += 1
        for target_course in edges[course]:
            edge_count[target_course] -= 1
            if edge_count[target_course] == 0:
                open_list.append(target_course)

    # Search is done, if all courses added to the list then possible
    # otherwise not possible -> return empty array
    if course_order_length == course_count:
        return course_order
    else:
        return []

def main():
    course_count = 4
    prerequisites = [
        [1, 0],
        [2, 0],
        [3, 1],
        [3, 2]
    ]
    print(course_schedule(course_count, prerequisites))

main()
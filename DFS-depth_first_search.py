from treelib import Node, Tree


def depth_first_search(graph, start, goal, visited=None, tree=None):
    if visited is None:
        visited = set()

    if tree is None:
        tree = Tree()
        tree.create_node(start, start)  # Root

    visited.add(start)
    print(f"Exploring node {start}")

    if start == goal:
        print(f"*** Goal {goal} found! ***")

    for neighbor in graph[start]:
        if neighbor not in visited:
            print(f"Exploring edge ({start}, {neighbor})")
            tree.create_node(neighbor, neighbor, parent=start)
            depth_first_search(graph, neighbor, goal, visited, tree)

    if start == tree.root:
        print(tree.show())


# Example
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': [],
    'G': [],
    'H': []
}

# Run the depth-first search
start = 'A'
goal = 'F'
print(f"Depth-First Search from node {start} to goal {goal}:")
depth_first_search(graph, start, goal)

from treelib import Node, Tree
from collections import deque


def breadth_first_search(graph, start, goal):
    visited = set()
    tree = Tree()
    tree.create_node(start, start)  # Root

    queue = deque([(start, tree.get_node(start))])

    while queue:
        node, tree_node = queue.popleft()
        visited.add(node)
        print(f"Exploring node {node}")

        if node == goal:
            print(f"*** Goal {goal} found! ***")
            break

        for neighbor in graph[node]:
            if neighbor not in visited:
                print(f"Exploring edge ({node}, {neighbor})")
                tree.create_node(neighbor, neighbor, parent=tree_node.identifier)
                queue.append((neighbor, tree.get_node(neighbor)))

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

# Run the breadth-first search
start = 'A'
goal = 'F'
print(f"Breadth-First Search from node {start} to goal {goal}:")
breadth_first_search(graph, start, goal)

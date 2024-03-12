import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

def draw_tree(tree_root, visited_nodes):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    node_colors = []
    for node_id in tree.nodes:
        if node_id in visited_nodes:
            # Generate unique color for each visited node based on its id
            color = "#{:06x}".format(int(node_id.replace('-', ''), 16) % 0xffffff)
        else:
            color = "skyblue"
        node_colors.append(color)

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

def dfs(node, visited):
    if node is None or node.id in visited:
        return
    visited.add(node.id)
    draw_tree(root, visited)  # Visualize the current state of the tree
    dfs(node.left, visited)
    dfs(node.right, visited)

def bfs(root):
    if root is None:
        return
    visited = set()
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.id not in visited:
            visited.add(node.id)
            draw_tree(root, visited)  # Visualize the current state of the tree
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

# Creating a binary tree
root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)

# Visualizing DFS (Depth-First Search)
dfs(root, set())

# Visualizing BFS (Breadth-First Search)
bfs(root)

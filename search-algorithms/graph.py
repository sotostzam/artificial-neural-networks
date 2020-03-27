import json, math

class Node:
    def __init__(self, value, x = None, y = None, obj = None):
        self.value = value
        self.discovered = False
        self.x = x
        self.y = y
        self.obj = obj

    # Rich comparison method called by x < y 
    def __lt__(self, other):
        # Returns priority based on alphabetical order
        return self.value < other.value

class Graph:
    def __init__(self):
        self.nodes        = []
        self.edges        = []

    # Function to fill graph from dataset
    def load_data(self, path, canvas):
        with open(path) as json_file:
            data = json.load(json_file)
            # Loop through the vertices
            for vertice in data:
                x_coord = data[vertice]['x']
                y_coord = data[vertice]['y']
                node = self.add_node(vertice, x_coord, y_coord, canvas)
                # Loop through the edges
                for edge in data[vertice]['Edges']:
                    # Loop through the keys (1 Iteration only)
                    for node_name in edge:
                        self.add_edge(node, self.add_node(node_name, data[node_name]['x'], data[node_name]['y'], canvas), edge[node_name], canvas)

    # Helper function to check regulate node's creation
    def add_node(self, value, x, y, canvas):
        for node in self.nodes:
            if node.value == value:
                return node
        obj = canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="grey")
        canvas.create_text(x + 40, y - 20, font="Purisa", text = value)
        new_node = Node(value, x, y, obj)
        self.nodes.append(new_node)
        return new_node
    
    # Helper function to check regulate edge's creation
    def add_edge(self, node1, node2, cost, canvas):
        for edge in self.edges:
            if edge[0] == node2 and edge[1] == node1:
                return False
        obj = canvas.create_line(node1.x, node1.y, node2.x, node2.y, width = 3, fill='black')
        self.edges.append((node1, node2, cost, obj))
        return True

    # Function returning a list of adjacent nodes
    def get_neighbors(self, node):
        neighbors = []
        for edge in self.edges:
            if node == edge[0]:
                neighbors.append((edge[1], edge[2]))
            if node == edge[1]:
                neighbors.append((edge[0], edge[2]))
        return neighbors

    # Helper function returning node object from name
    def get_node_obj(self, value):
        for node in self.nodes:
            if node.value == value:
                return node

    # Helper function to reset all nodes discovered status
    def reset_nodes(self):
        for node in self.nodes:
            if node.discovered:
                node.discovered = False

    # Heuristic function returning the distance from origin to target node
    def evaluate(self, node_1, node_2):
        distance = math.sqrt((node_2.x - node_1.x)**2 + (node_2.y - node_1.y)**2)   # Euclidean distance
        # distance = abs((node_1.x - node_2.x)) + abs((node_1.y - node_2.y))        # Manhattan distance
        return distance

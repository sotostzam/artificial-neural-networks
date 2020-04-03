import tkinter as tk

class Node():
    def __init__(self, value, pos, color, obj):
        self.value = value
        self.pos = pos
        self.color = color
        self.obj = obj
        self.neighbors = []

    def set_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

class Region():
    def __init__(self):
        # Window and canvas initialization parameters
        self.width  = 400
        self.height = 400
        self.window = tk.Tk()
        self.window.title("Australia Map coloring CSP")
        self.canvas = tk.Canvas(master = self.window, width = self.width, height = self.height, bg = "white")
        self.canvas.grid(row = 0, column = 0, sticky = "nsew")

        self.states = []
        self.lines  = []

    def get_node_obj(self, node):
        for item in self.states:
            if node is item.value:
                return item

    def populate(self):
        self.states.append(Node("WA", [70, 140], None, self.canvas.create_oval(45, 115, 95, 165, fill="white", outline="black", width = 2)))
        self.canvas.create_text(70, 140, font=("Purisa", 12), text = "WA", fill="black")
        self.states.append(Node("NT", [180, 90], None, self.canvas.create_oval(155, 65, 205, 115, fill="white", outline="black", width = 2)))
        self.canvas.create_text(180, 90, font=("Purisa", 12), text = "NT", fill="black")
        self.states.append(Node("SA", [190, 205], None, self.canvas.create_oval(165, 180, 215, 230, fill="white", outline="black", width = 2)))
        self.canvas.create_text(190, 205, font=("Purisa", 12), text = "SA", fill="black")
        self.states.append(Node("Q", [295, 115], None, self.canvas.create_oval(270, 90, 320, 140, fill="white", outline="black", width = 2)))
        self.canvas.create_text(295, 115, font=("Purisa", 12), text = "Q", fill="black")
        self.states.append(Node("NSW", [340, 210], None, self.canvas.create_oval(315, 185, 365, 235, fill="white", outline="black", width = 2)))
        self.canvas.create_text(340, 210, font=("Purisa", 12), text = "NSW", fill="black")
        self.states.append(Node("V", [275, 260], None, self.canvas.create_oval(250, 235, 300, 285, fill="white", outline="black", width = 2)))
        self.canvas.create_text(275, 260, font=("Purisa", 12), text = "V", fill="black")
        self.states.append(Node("T", [285, 330], None, self.canvas.create_oval(260, 305, 310, 355, fill="white", outline="black", width = 2)))
        self.canvas.create_text(285, 330, font=("Purisa", 12), text = "T", fill="black")

        self.get_node_obj("SA").set_neighbor(self.get_node_obj("WA"))
        self.get_node_obj("SA").set_neighbor(self.get_node_obj("NT"))
        self.get_node_obj("SA").set_neighbor(self.get_node_obj("Q"))
        self.get_node_obj("SA").set_neighbor(self.get_node_obj("NSW"))
        self.get_node_obj("SA").set_neighbor(self.get_node_obj("V"))
        self.get_node_obj("WA").set_neighbor(self.get_node_obj("NT"))
        self.get_node_obj("NT").set_neighbor(self.get_node_obj("Q"))
        self.get_node_obj("Q").set_neighbor(self.get_node_obj("NSW"))
        self.get_node_obj("NSW").set_neighbor(self.get_node_obj("V"))
        self.get_node_obj("V").set_neighbor(self.get_node_obj("T"))

        for state in self.states:
            neighbors = state.neighbors
            for neighbor in neighbors:
                exist = False
                for connection in self.lines:
                    if connection[0] is state and connection[1] is neighbor:
                        exist = True
                        break
                    elif connection[0] is neighbor and connection[1] is state:
                        exist = True
                        break
                if not exist:
                    self.lines.append((state, neighbor))
                    line = self.canvas.create_line(state.pos[0], state.pos[1], neighbor.pos[0], neighbor.pos[1], width = 2, fill = 'black')
                    self.canvas.tag_lower(line)

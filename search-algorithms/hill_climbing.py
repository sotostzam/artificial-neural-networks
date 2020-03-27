import math, time

def evaluate(node1, node2):
    item = math.sqrt((node2.x - node1.x)**2 + (node2.y - node1.y)**2)
    #item = abs((node1.x - node2.x)) + abs((node1.y - node2.y))
    return item

def search(graph, canvas, origin, target):
    # Make sure nodes are undiscovered initially
    graph.reset_nodes()
    origin_node = graph.get_node_obj(origin)
    target_node = graph.get_node_obj(target)
    # Hill climbing uses the node with the lowest distance to goal
    #frontier = (origin_node, graph.get_distance(origin_node), [origin_node.value], 0)
    frontier = (origin_node, evaluate(origin_node, target_node), [origin_node], 0)
    while frontier[0] != target_node:
        current_node, current_distance, path, total_cost = frontier

        ## Reset canvas
        for item in graph.nodes:
            canvas.itemconfig(item.obj, fill='grey')
        for item in graph.edges:
            canvas.itemconfig(item[3], width = 3, fill='black')

        for item in range(0, len(path)):
            canvas.itemconfig(path[item].obj, fill='red')
            canvas.tag_raise(path[item].obj)
            if item < len(path)-1:
                for edge in graph.edges:
                    if edge[0] == path[item] and edge[1] == path[item + 1] or edge[1] == path[item] and edge[0] == path[item + 1]:
                        canvas.itemconfig(edge[3], fill='red')
        canvas.update()
        time.sleep(0.5)

        neighbors = graph.get_neighbors(current_node)
        flag = False
        new_node = None
        if neighbors:
            new_cost = 0
            for neighbor_node, cost in neighbors:
                #neighbor_dist = graph.get_distance(neighbor_node)
                neighbor_dist = evaluate(neighbor_node, target_node)
                if neighbor_dist < current_distance:
                    new_node = neighbor_node
                    current_distance = neighbor_dist
                    new_cost = cost
                    flag = True
        else:
            return False
        if flag:
            total_cost += new_cost
            path.append(new_node)
            frontier = (new_node, current_distance, path, total_cost)
        else:
            return False
    
    # Reset canvas
    for item in graph.nodes:
        canvas.itemconfig(item.obj, fill='grey')
    for item in graph.edges:
        canvas.itemconfig(item[3], width = 3, fill='black')

    for item in range(0, len(path)):
        canvas.itemconfig(path[item].obj, fill='red')
        canvas.tag_raise(path[item].obj)
        if item < len(path)-1:
            for edge in graph.edges:
                if edge[0] == path[item] and edge[1] == path[item + 1] or edge[1] == path[item] and edge[0] == path[item + 1]:
                    canvas.itemconfig(edge[3], fill='red')
    canvas.update()
    time.sleep(0.5)

    return frontier[2], frontier[3]

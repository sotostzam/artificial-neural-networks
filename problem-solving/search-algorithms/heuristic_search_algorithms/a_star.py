import heapq

def search(graph, app, origin, target):
    origin_node = graph.get_node_obj(origin)
    target_node = graph.get_node_obj(target)
    # A* uses a priority queue as frontier. Priority is determined by the cost
    frontier = []
    # Frontier is a tuple of (priority, (node, path_to_node, total_cost))                    
    heapq.heappush(frontier, (0 + graph.evaluate(origin_node, target_node), (origin_node, [], 0)))
    while frontier:
        _ , state = heapq.heappop(frontier)
        current_node = state[0]
        current_path = state[1]
        current_cost = state[2]
        if current_node.discovered != True:
            current_node.discovered = True
            app.update_canvas(current_path, current_node)
            if current_node == target_node:
                current_path.append(current_node)
                return current_path, current_cost
            # Get neighbors of node and add them to frontier
            neighbors = graph.get_neighbors(current_node)
            for edge_node, cost in neighbors:
                if edge_node.discovered != True:
                    new_cost = current_cost + cost
                    new_path = current_path.copy()
                    new_path.append(current_node)
                    new_priority = new_cost + graph.evaluate(current_node, target_node)
                    heapq.heappush(frontier, (new_priority, (edge_node, new_path, new_cost)))
    # Return false if target is not found
    return False

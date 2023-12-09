
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def Deicstra(graph: dict, costs: dict, parents: dict):
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)


if __name__ == "__main__":
    g = {'start': {'A': 5, 'B': 2},
             'A': {'C': 4, 'D': 2},
             'B': {'A': 8, 'D': 7},
             'C': {'final': 3, 'D': 6},
             'D': {'final': 1},
             'final': {}}

    c = {'A': 5, 'B': 2, 'C': float('inf'), 'D': float('inf'), 'final': float('inf')}
    p = {'A': 'start', 'B': 'start', 'C': None, 'D': None, 'final': None}

    Deicstra(g, c, p)

    print(c['final'])

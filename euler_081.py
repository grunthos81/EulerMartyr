from time import time
from math import inf

grid = []
f = open("p081_matrix.txt", "r")
for line in f.readlines():
    grid.append([int(i) for i in line.strip().split(',')])


def dijkstra(start, graph, end):
    shortest_distance = {}

    unseen_nodes = {}
    for k, v in graph.items():
        unseen_nodes[k] = v
    for node in unseen_nodes:
        shortest_distance[node] = inf
    shortest_distance[start] = graph[0]['cost']

    while unseen_nodes:
        min_node = None
        for node in unseen_nodes:
            if min_node is None:
                min_node = node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node
        for neighbour in graph[min_node]['neighbours']:
            if graph[neighbour]['cost'] + shortest_distance[min_node] < shortest_distance[neighbour]:
                shortest_distance[neighbour] = graph[neighbour]['cost'] + shortest_distance[min_node]
        unseen_nodes.pop(min_node)
    if shortest_distance[end] != inf:
        return (shortest_distance[end])

def make_graph_81(size, grid):
    graph = {}
    count = 0
    for r in range(0, size):
        for c in range(0, size):
            if r == size -1 and c == size-1:
                graph[count] = {'cost' : grid[r][c], 'neighbours' : []}
            elif r == size-1:
                graph[count] = {'cost' : grid[r][c], 'neighbours' : [count+1]}
            elif c == size-1:
                graph[count] = {'cost' : grid[r][c], 'neighbours' : [count+size]}
            else:
                graph[count] = {'cost' : grid[r][c], 'neighbours' : [count+1, count+size]}
            count += 1
    return graph

def make_graph_83(size, grid):
    graph = {}
    count = 0
    for r in range(0, size):
        for c in range(0, size):
            if count == 6399: #bottom right corner - can't go anywhere
                graph[count] = {'cost' : grid[r][c], 'neighbours' : []}
            elif count == 0: #top left corner - down or right only
               graph[count] = {'cost' : grid[r][c], 'neighbours' : [count+size, count+1]} 
            elif count == 6320: #bottom left corner - up or right only
               graph[count] = {'cost' : grid[r][c], 'neighbours' : [count-size, count+1]} 
            elif count == 79: #top right corner - down and left only
               graph[count] = {'cost' : grid[r][c], 'neighbours' : [count+size, count-1]} 
            elif count < 80: #top row - can't go up
                graph[count] = {'cost' : grid[r][c], 'neighbours' : [count+1, count+size, count-1]}
            elif count > 6319: # bottom row - can't go down
                graph[count] = {'cost' : grid[r][c], 'neighbours' : [count+1, count-1, count-size]}
            elif count % 80 == 0: #left column - can't go left
                graph[count] = {'cost' : grid[r][c], 'neighbours' : [count+size, count-size, count+1]}
            elif c % 79 == 0: #right column - can't go right
                graph[count] = {'cost' : grid[r][c], 'neighbours' : [count+size, count-1, count-size]}
            else: #other squares can go anywhere
               graph[count] = {'cost' : grid[r][c], 'neighbours' : [count+size, count+1, count-1, count-size]} 
            count += 1
    return graph

start = time()
graph81 = make_graph_81(80, grid)
print(dijkstra(0, graph81, 6399), time()-start)

start = time()
graph83 = make_graph_83(80, grid)

print(dijkstra(0, graph83, 6399), time()-start)




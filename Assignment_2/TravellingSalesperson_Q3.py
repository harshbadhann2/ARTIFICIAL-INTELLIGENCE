list = adj_list = {
    1: [{2: 10}, {4: 20}, {3: 15}],
    2: [{1: 10}, {3: 35}, {4: 25}],
    3: [{1: 15}, {2: 35}, {4: 30}],
    4: [{1: 20}, {2: 25}, {3: 30}]
}

start = int(input("Enter the starting node (1-4): "))

visited = {1: False, 2: False, 3: False, 4: False}

#Marking that the starting node is visited

visited[start] = True
current_node = start
total_distance = 0
route = [current_node]

while len(route) < len(list):
    min_value = float("inf")
    next_node = None

    for neighbor in list[current_node]:
        for node, distance in neighbor.items():
            if visited[node] == False and distance < min_value:
                min_value = distance
                next_node = node

    if next_node is None:
        break

    visited[next_node] = True
    total_distance += min_value
    route.append(next_node)
    current_node = next_node

# to complete the cycle, return to the starting node
for neighbor in list[current_node]:
    for node, distance in neighbor.items():
        if node == start:
            total_distance += distance
            break

print("Optimal Route:", route)
print("Total Distance:", total_distance)




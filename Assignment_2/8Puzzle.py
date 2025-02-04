import heapq

class PuzzleSolver:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.rows = len(initial_state)
        self.cols = len(initial_state[0])

    def find_position(self, state, value):
        """Find the position (row, col) of a value in the puzzle."""
        for r in range(self.rows):
            for c in range(self.cols):
                if state[r][c] == value:
                    return r, c

    def manhattan_distance(self, state):

        distance = 0
        for r in range(self.rows):
            for c in range(self.cols):
                value = state[r][c]
                if value != 0:
                    goal_r, goal_c = self.find_position(self.goal_state, value)
                    distance += abs(r - goal_r) + abs(c - goal_c)
        return distance

    def get_neighbors(self, state):

        neighbors = []
        blank_r, blank_c = self.find_position(state, 0)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in moves:
            new_r, new_c = blank_r + dr, blank_c + dc
            if 0 <= new_r < self.rows and 0 <= new_c < self.cols:
                # Swap blank tile with the neighbor
                new_state = [row[:] for row in state]
                new_state[blank_r][blank_c], new_state[new_r][new_c] = new_state[new_r][new_c], new_state[blank_r][blank_c]
                neighbors.append(new_state)

        return neighbors

    def solve(self):

        # Priority queue for A* search
        pq = []
        # Initial state
        heapq.heappush(pq, (0 + self.manhattan_distance(self.initial_state), 0, self.initial_state, []))
        visited = set()

        while pq:
            _, cost, current_state, path = heapq.heappop(pq)

            # Check if we've reached the goal
            if current_state == self.goal_state:
                return path

            # Mark the current state as visited
            visited.add(tuple(tuple(row) for row in current_state))

            # Generate neighbors
            for neighbor in self.get_neighbors(current_state):
                if tuple(tuple(row) for row in neighbor) not in visited:
                    new_cost = cost + 1
                    heuristic = self.manhattan_distance(neighbor)
                    heapq.heappush(pq, (new_cost + heuristic, new_cost, neighbor, path + [neighbor]))

        return None



initial_state = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]
goal_state = [
    [2, 8, 1],
    [0, 4, 3],
    [7, 6, 5]
]

solver = PuzzleSolver(initial_state, goal_state)
solution = solver.solve()

if solution:
    print("Solution found:")
    for step, state in enumerate(solution, 1):
        print(f"Step {step}:")
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")

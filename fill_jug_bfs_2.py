print("Fill the Jug ")

CAP_A = 4
CAP_B = 3

# Goal Amount
GOAl =2

# Function to print the class
def print_state(state):
    print("Jug A:", state[0], "liters")
    print("Jug B:", state[1], "liters")
    print()


#Generate all posible moves
def get_neighbors(state):
    neighbors = []

    a, b = state

    #1.Fill Jug A
    if a< CAP_A:
        neighbors.append(((CAP_A, b),"Fill Jug A"))

    #2.Fill Jug B
    if b< CAP_B:
        neighbors.append(((a, CAP_B),"Fill Jug B")) 

    #3.Empty Jug A
    if b>0:
        neighbors.append(((0, b),"Empty Jug A"))  
    
    #4.Empty Jug B
    if b>0:
        neighbors.append(((a, 0),"Empty Jug B"))  

    #5.pour Jug A -> Jug B
    amount = min(a, CAP_B - b)

    if amount > 0:
        neighbors.append(
            ((a - amount, b + amount),
             "Pour Jug A -> Jug B")
             )

    #6. Pour Jug B -> Jug A
    amount = min(b, CAP_A - a)

    if amount > 0:
        neighbors.append(
            ((a + amount, b - amount),
             "Pour Jug B -> Jug A")
        )

    return neighbors

#BFS Algorithm
def bfs(start):
    queue = [(start, [])]
    visited = set()

    while queue:
        start, path = queue.pop(0)

        if state in visited:
            continue
            
        visited.add(state)

    # Check Goal 
    if state[0] == GOAl or state[1] == GOAl:
        return path + [(state, "Goal Reached:")]
    #Ganerte Neighbors
    for  neighbor, action in get_neighbors(state):

        if neighbor not in visited:
            queue.append(
                (neighbor, path + [(neighbor, action)])
            )

    return None
#starting State
start = (0, 0)


# run BFS
solution = bfs(start)

#print Solution
if solution:
    print("Solution Found in", len(solution) -1,"moves:\n")

    print("Initial State:")
    print_state(start)

    for state, action in solution:
        print(action)
        print_state(state)

else:
    print("No Solution Found here.")

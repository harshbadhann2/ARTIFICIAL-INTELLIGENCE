def water_jug_problem(capacity_a, capacity_b, target):
    a, b = 0, 0
    print(f"Initial state: Jug A: {a}, Jug B: {b}")
    while (a != target and b != target):
        if a == 0:
            # fill jug a if it is empty
            a = capacity_a
            print(f"Fill jug A: {a}, jug B: {b}")
        elif b == capacity_b:
            b = 0
            print(f"Empty jug B: jug A: {a}")
        else:
            # pour water from jug a to jug B
            pour = min(a, capacity_b - b)
            a -= pour
            b += pour
            print(f"Pour water from Jug A to Jug B: Jug a: {a}, jug b: {b}")
    print(f"Target reached Jug A: {a}, Jug B: {b}")


if __name__ == "__main__":
    capacity_a = int(input("Enter the capacity of jug A"))
    capacity_b = int(input("Enter the capacity of jug B"))
    target = int(input("Enter target"))
    water_jug_problem(capacity_a, capacity_b, target)
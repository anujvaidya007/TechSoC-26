import sys
def sorting(n, containers):
    new_order = containers.copy()
    for i in range(0, n):
        for j in range(0, n-1-i):
            if new_order[j+1] < new_order[j]:
                k = new_order[j]
                new_order[j] = new_order[j+1]
                new_order[j+1] = k
    print("Heaviest container:", new_order[n-1])
    print("Lightest container:", new_order[0])
    print("Containers in sorted order:")
    printed = []
    for x in range(0, n):
        for i in range(0, n):
            if containers[i] == new_order[x] and i not in printed:
                print("W", i+1, ":", new_order[x])
                printed.append(i)
                break
    return new_order
def bar_graph(n, s, containers, new_order, name, data):
    if s == 0:
        print("Cannot create graph because total weight is 0")
    else:
        for x in range(0, n):
            print("W", x+1, "* " * int(containers[x]*10*n/s))
    process(n, s, containers, new_order, name, data)
def searching(n, s, containers, new_order, name, data):
    print("What is the weight of the container that you want to search")
    w = int(input())
    f = 0
    for x in range(0, n):
        if containers[x] == w:
            print("The container is W", x+1)
            f += 1
    if f == 0:
        print("No such container found")
    process(n, s, containers, new_order, name, data)
def kth_heaviest(n, s, containers, new_order, name, data):
    print("What is the value of k")
    k = int(input())
    if k <= n and k > 0:
        target_weight = new_order[n-k]
        printed = []
        for i in range(0, n):
            if containers[i] == target_weight and i not in printed:
                print("The", k, "th heaviest container is W", i+1,
                      "with weight", containers[i])
                printed.append(i)
                break
    else:
        print("Enter a valid number")
        kth_heaviest(n, s, containers, new_order, name, data)
        return
    process(n, s, containers, new_order, name, data)
def data_saved(n, s, containers, new_order, name, data):
    filename = name + ".txt"
    with open(filename, "w") as file:
        # Port capacity
        file.write(str(data[0]) + "\n")
        # Number of containers
        file.write(str(data[1]) + "\n")
        # Container weights
        for weight in containers:
            file.write(str(weight) + "\n")
        # Shipment identity
        file.write(name + "\n")
    print("Shipment data saved successfully in", filename)
def process(n, s, containers, new_order, name, data):
    print()
    print("What data do you want to know further")
    print("1 : Show a bar graph for the weight of the containers")
    print("2 : Search for a container with some weight")
    print("3 : Find the kth heaviest container")
    print("4 : Display sorted containers")
    print("x : Exit this shipment procedure and save data")
    pro = input()
    if pro == '1':
        bar_graph(n, s, containers, new_order, name, data)
    elif pro == '2':
        searching(n, s, containers, new_order, name, data)
    elif pro == '3':
        kth_heaviest(n, s, containers, new_order, name, data)
    elif pro == '4':
        new_order = sorting(n, containers)
        process(n, s, containers, new_order, name, data)
    elif pro == 'x' or pro == 'X':
        data_saved(n, s, containers, new_order, name, data)
        print()
        print("A : Process a new shipment")
        print("X : Recall an existing shipment")
        print("Q : Exit program")
        g = input()
        if g == 'Q' or g == 'q':
            sys.exit()
        elif g == 'A' or g == 'a':
            shipment_data_processing()
        elif g == 'X' or g == 'x':
            shipment_data_recall()
        else:
            print("Enter a valid input")
            main_program()
    else:
        print("Enter a valid input")
        process(n, s, containers, new_order, name, data)
def shipment_data_processing():
    print("Enter identity or name of the ship")
    name = input()
    print("Enter max port capacity")
    C = int(input())
    print("Enter the number of containers")
    N = int(input())
    if N <= 0:
        print("Number of containers must be greater than 0")
        shipment_data_processing()
        return
    container = [0] * N
    for x in range(0, N):
        print("Enter weight of W", x+1, "container")
        container[x] = int(input())
    S = 0
    for x in range(0, N):
        S += container[x]
    new_order = sorting(N, container)
    print()
    print("Total Shipment Weight:", S)
    print("Average Container Weight:", S/N)
    if S > 200:
        print("Classification: Heavy")
    else:
        print("Classification: Light")
    print("Port Capacity:", C)
    if S > C:
        print("Shipment exceeds port capacity")
    else:
        print("Shipment can be unloaded")
    data = [C, N, container]
    process(N, S, container, new_order, name, data)
def shipment_data_recall():
    print("What is the identity of the shipment")
    name = input()
    filename = name + ".txt"
    try:
        with open(filename, "r") as file:
            c = int(file.readline())
            n = int(file.readline())
            containers = []
            for x in range(0, n):
                containers.append(int(file.readline()))
            name = file.readline().strip()
    except FileNotFoundError:
        print("No shipment with this identity was found")
        main_program()
        return
    except ValueError:
        print("Shipment file contains invalid data")
        main_program()
        return
    data = [c, n, containers]
    S = 0
    for x in range(0, n):
        S += containers[x]
    new_order = sorting(n, containers)
    print()
    print("Shipment identity:", name)
    print("Total Shipment Weight:", S)
    print("Average Container Weight:", S/n)
    if S > 200:
        print("Classification: Heavy")
    else:
        print("Classification: Light")
    print("Port Capacity:", c)
    if S > c:
        print("Shipment exceeds port capacity")
    else:
        print("Shipment can be unloaded")
    process(n, S, containers, new_order, name, data)
def main_program():
    print()
    print("A : Enter new shipment data")
    print("X : Check existing shipment data")
    print("Q : Exit program")
    task = input()
    if task == 'A' or task == 'a':
        shipment_data_processing()
    elif task == 'X' or task == 'x':
        shipment_data_recall()
    elif task == 'Q' or task == 'q':
        sys.exit()
    else:
        print("Enter a valid input")
        main_program()
print("CONTAINER SHIPMENT DATA PROCESSING SYSTEM")
main_program()
        
        
        
    
    
    

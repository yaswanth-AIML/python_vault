import networkx as nx
import matplotlib.pyplot as plt

def build_graph():
    h = []
    num = int(input("Enter The Total Number Of Edges: "))
    weighted = input("Do you want to enter weights? (yes/no): ").lower()

    for i in range(1, num+1):
        v1 = input(f"Enter Vertex 1 for Edge {i}: ")
        v2 = input(f"Enter Vertex 2 for Edge {i}: ")
        if weighted == "yes":
            weight = int(input("Add The Weight Also: "))
            h.append((v1, v2, weight))
        else:
            h.append((v1, v2))

    if weighted == "yes":
        G = nx.Graph()
        G.add_weighted_edges_from(h)
    else:
        G = nx.Graph()
        G.add_edges_from(h)

    return G, weighted == "yes"
def choose_layout(G):
    print("\nChoose Layout:")
    print("1. Spring Layout")
    print("2. Circular Layout")
    print("3. Random Layout")
    print("4. Planar Layout")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        return nx.spring_layout(G)
    elif choice == 2:
        return nx.circular_layout(G)
    elif choice == 3:
        return nx.random_layout(G)
    elif choice == 4:
        return nx.planar_layout(G)
    else:
        print("Invalid choice, using spring layout.")
        return nx.spring_layout(G)

def visualize_graph(G, pos, weighted):
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray")
    if weighted:
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

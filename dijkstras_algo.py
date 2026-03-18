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

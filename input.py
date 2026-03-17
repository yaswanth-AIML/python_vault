def input_user1():
    while True:
        try:
            num=int(input("Enter The Total Number Of Edges: "))
        except:
            print("'ENTER THE NUMBER'")
        else:
            for i in range(1,num+1):
                verter1=input(f"Enter Vertex 1 for Edge {i}: ")
                vertex2=input(f"Enter Vertex 2 for Edge {i}: ")
                try:
                    weight=int(input("Add The Weight Also: "))
                except:
                    print("ENTER THE NUMBER FOR WEIGHT")
                else:
                    h.append((verter1,vertex2,weight))
            print(h)
            g=nx.Graph()
            g.add_weighted_edges_from(h)
            pos = nx.spring_layout(g)
            nx.draw(g, pos, with_labels=True)
            labels = nx.get_edge_attributes(g,'weight')
            nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
            break

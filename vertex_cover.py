import networkx as nx
import matplotlib.pyplot as plt
import random 
import time 
def create_vertices(n):
    vert=[]
    for i in range(n):
        vert.append(i)
    return vert
def create_edge(m,n,v):
    if m<n-1:
        print("Insufficient Edges!")
        return []
    if m > (n*(n-1))/2:
        print("Too many edges for simple graph!")
        return []
    all_edges=[]
    connected=[]
    connected.append(v[0])
    for i in v[1:]:
        target = random.choice(connected)
        all_edges.append((i,target))
        connected.append(i)
    while len(all_edges)<m:
        first = random.choice(connected)
        second = random.choice(connected)
        if first not in range(n) or second not in range(n):
            print("Invalid vertex")
            continue
        if first==second:
            print("Self loop is not allowed")
            continue
        if (first, second) in all_edges or (second, first) in all_edges:
            print("Duplicate Edge")  
            continue 
        pair = (first , second)
        all_edges.append(pair)
    return all_edges
def power_set(v):
    all_subset = []
    for number in range(2**(len(v))):
        subset=[]
        for i in range(len(v)):
            if number & (1<<i):
                subset.append(i)
        all_subset.append(subset)
    return all_subset
def brute_vertex_cover(s,e):
    vertex_cover =[]
    minimum_cover = None
    for subset in s:
        is_cover = True
        for edge in e:
            if edge[0] not in subset and edge[1] not in subset:
                is_cover = False
                break
        if is_cover:
            vertex_cover.append(subset)
            if minimum_cover is None:
                minimum_cover = subset
            if len(subset)<len(minimum_cover):
                minimum_cover=subset
    return minimum_cover
def display_graph(v,e,vc, filename):
    G = nx.Graph()
    G.add_nodes_from(v)
    G.add_edges_from(e)
    node_colors = []
    for i in v:
        if i in vc:
            node_colors.append("Orange")
        else:
            node_colors.append("Blue")
    nx.draw(G , with_labels=True, node_color = node_colors, font_size=12)
    plt.savefig(filename)
    plt.show()
    plt.close()
with open("output.txt", "w") as output_file:
    for i in range(1,9):
        with open(f"input{i}.txt","r") as input_file:
            first_line = input_file.readline()
            parts = first_line.strip().split(" ")
            n = int(parts[0])
            m = int(parts[1])
        print(f"No. of vertices: {n} and No of edges: {m}")
        c = create_vertices(n)
        v = list(c)
        random.shuffle(v)
        print("Original Vertices:", c)
        print("Shuffled Vertices: ", v)
        e = create_edge(m,n,v)
        print("Edges are: ", e)
        start_time = time.time()
        s=power_set(v)
        print("Power set :", s)
        vc = brute_vertex_cover(s,e)
        print("Vertex Cover:", vc)
        end_time = time.time()
        execution_time = (end_time - start_time)* 1000
        print("Execution Time :", execution_time, "ms")
        output_file.write(f"\n========== INPUT {i} ==========\n")
        output_file.write(f"No. of Vertices: {n}\n")
        output_file.write(f"No.of edges: {m}\n")
        output_file.write(f"Original vertices: {c}\n")
        output_file.write(f"Shuffled vertices:{v}\n")
        output_file.write(f"Edges: {e}\n")
        output_file.write(f"Power set: {s}\n")
        output_file.write(f"Vertex cover: {vc}\n ")
        output_file.write(f"Execution Time (in milliseconds): {execution_time}")
        display_graph(c,e, vc, f"graph{i}.png")


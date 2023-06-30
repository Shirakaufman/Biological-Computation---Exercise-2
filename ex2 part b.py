import math
import itertools
import networkx as nx
import time as time


#Biological computation-ex2:
# shira landau-208275248
#PART B:

def create_graph():
    graph = nx.DiGraph()
    node = int(input("Please enter n: "))
    x = input("Please enter nodes in the following format: x,y (enter -1 to finish adding)\n")
    while x != "-1":
        graph.add_edge(int(x[0]), int(x[2]))
        x=input()
    return graph, node
def create_all_possible_graphs(n):#from partA
    edges = n * (n - 1)
    z = pow(2, edges)
    bits = str('0') + str(edges) + str('b')
    allPos = [[0] for _ in range(z + 1)]

    for i in range(z):
        allPos[i] = format(i, bits)

    allPairs = list(itertools.combinations(range(1, n + 1), 2))
    allGraphs = [[0] for _ in range(z)]

    for i in range(z):
        allGraphs[i] = nx.DiGraph()
        for j in range(0, edges):
            if int(allPos[i][j]) == 1:
                if j <= ((edges / 2) - 1):
                    allGraphs[i].add_edge(allPairs[j][0], allPairs[j][1])
                else:
                    m = int(j - (edges / 2))
                    allGraphs[i].add_edge(allPairs[m][1], allPairs[m][0])

    return allGraphs, allPos,z
def create_all_sub_graphs(node,graph):#for graph 
    edges = len(graph.edges)
    new_z = pow(2, edges)
    bits = str('0') + str(edges) + str('b')
    pos = [[0] for y in range(new_z)]

    for i in range(new_z):
        pos[i] = format(i, bits)

    sub_graphs = [[0] for y in range(new_z)]
    allPairs = list(graph.edges)
    for i in range(new_z):
        sub_graphs[i] = nx.DiGraph()
        for j in range(edges):
            if int(pos[i][j]) == 1:
                sub_graphs[i].add_edge(allPairs[j][1], allPairs[j][0] )

    # filter all graphs that are not n size
    i = 0
    while i < new_z:
        if len(sub_graphs[i].nodes) != node:
            del sub_graphs[i]
            new_z -= 1
        else:
            i += 1
    return sub_graphs
def filter_graphs(allGraphs,allPos,z,n): #from partA
#apply filters to identify isomorphic graphs, removing graphs with less than n connected nodes, and excluding all non-n connected graphs."
    i = 0
    while i < z:
        j = i + 1
        while j < z:
            if nx.is_isomorphic(allGraphs[i], allGraphs[j]):
                del allGraphs[j],allPos[j]
                z -= 1
            else:
                j += 1
        i += 1

    j = 0
    while j < z:
        if len(allGraphs[j].nodes) != n:
            del allGraphs[j], allPos[j]
            z -= 1
        else:
         j += 1

    j = 0
    while j < z:
        if not nx.is_empty(allGraphs[j]):
            if not nx.is_weakly_connected(allGraphs[j]):
                del allGraphs[j], allPos[j]
                z -= 1
        j += 1

    return allGraphs,z
def count_isomorphic_graphs(z,sg,node,filtered_graphs):  # count isomorphic graphs
    posCount = [0] * z
    for i in range(z):
        for j in range(len(sg)):
            if nx.is_isomorphic(filtered_graphs[i], sg[j]):
                posCount[i] += 1
    return posCount
def write_output_to_file(z,countGraphs,filtered_graphs,node):
    partb_file = open(r"C:\Users\shira\Documents\partB.txt", "w")
    partb_file.write("n=" + str(node) + "\n")
    partb_file.write("graph count=" + str(len(filtered_graphs)) + "\n")
    for i in range(z):
        partb_file.write("#" + str(i + 1) + "   count=" + str(countGraphs[i]) + "\n")
        for edge in filtered_graphs[i].edges:
            partb_file.write(str(edge[0]) + " " + str(edge[1]) + "\n")

    partb_file.close()
def run_partB() :
    graph, node = create_graph()
    allGraphs,allPos,z = create_all_possible_graphs(node)
    subGraphs=create_all_sub_graphs(node,graph) 
    filtered_graphs,z = filter_graphs(allGraphs,allPos,z,node)
    countGraphs=count_isomorphic_graphs(z,subGraphs,node,filtered_graphs)
    write_output_to_file(z,countGraphs,filtered_graphs,node)

if __name__ == "__main__":
    run_partB()



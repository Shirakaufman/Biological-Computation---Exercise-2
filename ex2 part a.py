#Biological computation-ex2:
# shira landau-208275248

import itertools
import networkx as nx
import time as time

# Part A
def create_all_possible_graphs(n):
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

    return allGraphs,allPos,z
def filter_graphs(allGraphs,allPos,z,n):
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

    filtered_graphs = []
    
    # Filter graphs with less than n connected nodes
    for i in range(len(graphs)):
        if len(graphs[i].nodes) == n and nx.is_weakly_connected(graphs[i]):
            filtered_graphs.append(graphs[i])

    return filtered_graphs
def write_graphs_to_file(graphs, n):
    graph_file = open("sub-graphs with {} nodes.txt".format(n), "w")
    graph_file.write("n={}\n".format(n))
    graph_file.write("count={}\n".format(len(graphs)))

    for i in range(len(graphs)):
        graph_file.write("#{}\n".format(i + 1))
        for edge in graphs[i].edges:
            graph_file.write("{} {}\n".format(edge[0], edge[1]))

    graph_file.close()

def run_partA(n):
    allGraphs,allPos,z  = create_all_possible_graphs(n)
    filtered_graphs,z = filter_graphs(allGraphs,allPos,z,n)
    write_graphs_to_file(filtered_graphs,n)

def check_time():
    #part c+d check how long time :
    time_file = open("PartA_times.txt", "w") 
    one_hour,two_hours,four_hours,eight_hours = "","","",""
    n=1
    endTime=0
    while(endTime<8):
        startTime = time.time()
        run_partA(n)
        endTime = (time.time() - startTime) / 3600
        if  endTime < 1:
            one_hour=str(n) 
        if endTime > 1 and endTime < 2:
            two_hours = str(n) 
        if endTime > 2 and endTime< 4:
            four_hours =str(n) 
        if endTime>4 and endTime<8:
            eight_hours=str(n)
        n+=1      
        
    time_file.write("the max n can complete in one hour is "+one_hour+"\n")
    time_file.write("the max n can complete in 2 hours is "+two_hours+"\n")
    time_file.write("the max n can complete in  4 hours is "+four_hours+"\n")
    time_file.write("the max n can complete in 8 hours is "+eight_hours+"\n")
    
if __name__ == "__main__":
    n = int(input("Please enter n: "))
    run_partA(n)
    check_time()

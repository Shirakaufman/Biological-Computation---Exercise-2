# Biological-Computation---Exercise-2

by:
shira landau-208275248

# PART A:
This code is a program written in Python that generates all connected sub-graphs of a given size, n. The program utilizes the networkx library for graph operations and itertools for combinations. The generated sub-graphs are then written to a textual file in a specific format.

Function Descriptions
create_all_possible_graphs(n)
This function creates all possible graphs of size n. It generates a list of all possible binary strings representing edges, and then converts them into graph representations using networkx's DiGraph class. The function returns a tuple containing the list of all graphs, the binary strings, and the total number of graphs generated.

filter_graphs(allGraphs, allPos, z, n)
This function applies filters to the generated graphs to remove isomorphic graphs, graphs with less than n connected nodes, and non-n connected graphs. It modifies the input lists to remove the filtered graphs and returns the updated lists and the new total number of graphs.

write_graphs_to_file(graphs, n)
This function writes the filtered graphs to a textual file in the specified format. It opens a file with a name based on the size of the sub-graphs and writes the count of sub-graphs followed by the graph representations.

run_partA(n)
This function is the main driver function for generating and writing the sub-graphs. It calls the create_all_possible_graphs function to generate all possible graphs, then filters them using the filter_graphs function. Finally, it writes the filtered graphs to a file using the write_graphs_to_file function.

check_time()
This function measures the time taken to execute run_partA(n) for different values of n. It determines the maximum value of n that can be completed within specific time intervals (1 hour, 2 hours, 4 hours, and 8 hours). The results are written to a file named "PartA_times.txt".

Task Execution
To execute the program, run the script and enter a positive integer n as input. The program will generate and write the sub-graphs of size n to a file. Additionally, it will measure the execution time for different values of n and write the results to the "PartA_times.txt" file.

For the given task:

a)
The program generates all connected sub-graphs of size n and writes them to a textual file in the specified format.
b)
The output of the program for n = 1 to 4 will be available in separate files named "sub-graphs with 1 nodes.txt", "sub-graphs with 2 nodes.txt", "sub-graphs with 3 nodes.txt", and "sub-graphs with 4 nodes.txt
c+d)
The maximum value of 'n' for which the code can complete in an hour is found to be n=4. Additionally, if we allow the code to run for up to 2 hours, it can handle n=5. However, when trying to run the code for n=6, it didn't finish running even after eight hours. Therefore, the final conclusion is that for 2 hours-8 hours  the optimal value for 'n' is determined as 5.

# PART B:
This code is a Python program designed to analyze a given graph and identify all sub-graphs of a specified size, n. The program counts the occurrences of each sub-graph motif and outputs the results in a specific format.

Function Descriptions
create_graph()
This function prompts the user to input the number of vertices and the edges of a graph in a specific format. It creates and returns a directed graph using the networkx library.

create_all_possible_graphs(n)
This function is adapted from Part A. It generates all possible graphs of size n using binary strings and combinations. It returns a tuple containing the list of all graphs, the binary strings, and the total number of graphs generated.

create_all_sub_graphs(node, graph)
This function generates all sub-graphs of size n from the given graph. It creates a binary string representation of all possible sub-graphs and filters out the ones that do not have n nodes. It returns a list of all valid sub-graphs.

filter_graphs(allGraphs, allPos, z, n)
This function is adapted from Part A. It applies filters to the generated graphs to remove isomorphic graphs, graphs with fewer than n connected nodes, and non-n connected graphs. It modifies the input lists to remove the filtered graphs and returns the updated lists and the new total number of graphs.

count_isomorphic_graphs(z, sg, node, filtered_graphs)
This function counts the occurrences of each sub-graph motif in the filtered graphs. It compares each filtered graph with all sub-graphs and increments the count when an isomorphic match is found. It returns a list containing the counts for each motif.

write_output_to_file(z, countGraphs, filtered_graphs, node)
This function writes the analysis results to a file named "partB.txt". It includes the number of nodes in the graph, the count of distinct sub-graphs, and the counts of each motif along with their respective edges.

run_partB()
This function serves as the main driver for the program. It calls the necessary functions in the proper order to analyze the graph and generate the output.

Task Execution
To execute the program, run the script. The program will prompt for input to provide the graph information. After receiving the input, it will analyze the graph, identify the sub-graphs of size n, count the motifs, and write the results to a file named "partB.txt".

For the given task:

The program takes a positive integer n as input, along with a graph in the specified format. It identifies all sub-graphs of size n and counts the occurrences of each motif. The results are written to the "partB.txt" file in the required format.
ב(

# Hypergraph-Coloring

Explanation and Documentation:

#include <bits/stdc++.h>: This line includes necessary standard libraries, including <iostream>, <vector>, and other essential libraries.
class hg: This line begins the declaration of the hg class, which encapsulates the hypergraph and related operations.
Member Variables:
int vertices, edges, colors_used;: These variables store the number of vertices, edges, and colors used in the hypergraph.
bool sorted_status;: This boolean indicates whether the hypergraph is sorted based on vertex degrees.
vector<vector<int>> hypergraph;: A 2D vector to store the hypergraph.
vector<vector<int>> hypergraph_sorted;: A 2D vector to store the sorted hypergraph.
vector<int> vertex_degrees;: A vector to store the degrees of each vertex.
vector<int> vertex_colors;: A vector to store the colors assigned to vertices.
hg(int v, int e): Constructor to initialize the hypergraph with the specified number of vertices and edges.
void print_hg(): Function to print the hypergraph.
void sort(): Function to sort the hypergraph based on descending vertex degrees and compute vertex degrees.
int dot_prod(int v1, int v2): Function to compute the dot product of hypergraph vertices.
int main(): The main function where the program starts execution.
It prompts the user to enter the number of vertices and edges.
Creates an instance of the hg class using the input vertices and edges.
Calls print_hg() to print the original hypergraph.
Calls sort() to sort the hypergraph based on vertex degrees and print the sorted hypergraph using print_hg().

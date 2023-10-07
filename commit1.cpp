#include <bits/stdc++.h> // Include necessary standard libraries
using namespace std;

class hg {
public:
  int vertices, edges,
      colors_used; // Variables to store vertices, edges, and colors used
  // Number of vertices, edges, colors_used in coloring

  bool sorted_status; // Boolean indicating whether the hypergraph is sorted
  // Whether the hypergraph has been sorted in order of decreasing vertex
  // degrees

  vector<vector<int>> hypergraph; // 2D vector to store the hypergraph
  vector<vector<int>>
      hypergraph_sorted; // 2D vector to store the sorted hypergraph

  vector<int> vertex_degrees; // Vector to store the degrees of each vertex

  vector<int> vertex_colors; // Vector to store the colors assigned to vertices

  hg(int v, int e) { // Constructor to initialize the hypergraph with vertices
                     // and edges
    vertices = v;    // Assign the number of vertices
    edges = e;       // Assign the number of edges
    colors_used = 0; // Initialize the number of colors used to 0
    sorted_status = false; // Initialize sorted status to false

    // Input values for the hypergraph
    for (int vertex = 0; vertex < v; vertex++) {
      vector<int> row;
      cout << "Enter vertex"<< vertex << endl;
      for (int edge = 0; edge < edges + 1; edge++) {
        int value;
        
        cin >> value;         // Read input value for the hypergraph
        row.push_back(value); // Add the value to the current row
      }
      hypergraph.push_back(row); // Add the row to the hypergraph
    }
  }

  void print_hg() { // Function to print the hypergraph
    for (int vertex = 0; vertex < vertices; vertex++) {
      for (int edge = 0; edge < edges + 1; edge++) {
        cout << hypergraph[vertex][edge]
             << " "; // Print each value in the hypergraph
      }
      cout << endl; // Move to the next line for the next vertex
    }
  }

  void sort() {
    // Function to sort the hypergraph and compute vertex degrees

    // Compute degrees for each vertex
    for (int vertex = 0; vertex < vertices; vertex++) {
      int degree = 0;
      for (int edge = 1; edge < edges + 1; edge++) {
        degree += hypergraph[vertex][edge]; // Compute the degree of the vertex
      }
      cout << "Degree of vertex " << vertex << ": " << degree << endl;
      vertex_degrees.push_back(
          degree); // Store the degree in the vertex_degrees vector
    }

    // sorting hypergraph vertices according to vertex degrees
    
    for (int i = 0; i < vertices - 1; i++) {
      for (int j = i + 1; j < vertices; j++) {
        if (vertex_degrees[i] < vertex_degrees[j]) {
          int temp = vertex_degrees[i];
          vertex_degrees[i] = vertex_degrees[j];
          vertex_degrees[j] = temp;

          vector<int> temp_vertex = hypergraph[i];
          hypergraph[i] = hypergraph[j];
          hypergraph[j] = temp_vertex;
        }
      }
    }

    sorted_status = true; // Set the sorted status to true
    // hypergraph_sorted = hypergraph; // Copy the original hypergraph to the
    // sorted hypergraph
  }

  int dot_prod(int v1, int v2) {
    // Function to compute the dot product of hypergraph vertices
    int ans = 0;
    for (int edge = 1; edge < edges; edge++) {
      ans += hypergraph[v1][edge] * hypergraph[v2][edge]; // Compute dot product
    }
    return ans; // Return the dot product
  }
};

int main() {
  // Main function
  int v,e;
  cout<<"Enter number of vertices"<<endl;
  cin>>v;
  cout<<"Enter number of edges"<<endl;
  cin>>e;
  
  hg hg1 = hg(v,e); // Create an instance of the hg class with 3 vertices and 2 edges
  hg1.print_hg(); // Print the original hypergraph
  hg1.sort();     // Sort the hypergraph and compute vertex degrees
  hg1.print_hg(); // Print the sorted hypergraph
  
}

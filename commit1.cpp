#include <bits/stdc++.h>
using namespace std;

class hg {
public:
  int vertices, edges, colors_used;
  // Number of vertices, edges, colors_used in coloring
  bool sorted_status;
  // Whether the hypergraph has been sorted in order of decreasing vertx degrees
  vector<vector<int>> hypergraph;

  vector<vector<int>> hypergraph_sorted;

  vector<int> vertex_degrees;

  vector<int> vertex_colors;

  hg(int v, int e) {
    vertices = v;
    edges = e;
    colors_used = 0;
    sorted_status = false;

    for (int vertex = 0; vertex < v; vertex++) {
      vector<int> row;
      for (int edge = 0; edge < edges+1; edge++) {
        int value;
        cout << "Enter value" << endl;
        cin >> value;
        row.push_back(value);
      }
      hypergraph.push_back(row);
    }

    // int hypergraph[v][e];
  }

  void print_hg() {
    // cout<<hypergraph[0][0];

    for (int vertex = 0; vertex < vertices; vertex++) {
      for (int edge = 0; edge < edges+1; edge++) {
        cout << hypergraph[vertex][edge] << " ";
      }
      cout << endl;
    }
  }

  void sort() {
    sorted_status = true;
    for (int vertex = 0; vertex < vertices; vertex++) {
      int degree = 0;
      for (int edge = 1; edge < edges+1; edge++) {
        degree += hypergraph[vertex][edge];
      }
      cout<<degree<<endl;
      vertex_degrees.push_back(degree);
    }

    hypergraph_sorted = hypergraph;
    // copy
  }

  int dot_prod(int v1, int v2)
{
  int ans = 0;
  for (int edge = 1; edge<edges; edge++)
    {
      ans += hypergraph[v1][edge] * hypergraph[v2][edge];
    }
  return ans;
}
  
};

  int main() {
    hg hg1 = hg(3, 2);
    hg1.print_hg();
    hg1.sort();
    cout<<hg1.dot_prod(0, 1);
  }

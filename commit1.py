class Hypergraph:
    def __init__(self, v, e):
        # Initialize the Hypergraph class with given vertices (v), edges (e), and other necessary variables.
        self.vertices = v
        self.edges = e
        self.colors_used = 0
        self.sorted_status = False
        self.hypergraph = []  # Initialize an empty list to store the hypergraph.
        self.hypergraph_sorted = []  # Initialize an empty list to store the sorted hypergraph.
        self.vertex_degrees = []  # Initialize an empty list to store vertex degrees.
        self.vertex_colors = []  # Initialize an empty list to store vertex colors.

        # Collect information about the hypergraph from the user.
        for vertex in range(v):
            row = []  # Initialize an empty list for the current vertex (row).
            print("Enter vertex", vertex + 1)
            for edge in range(self.edges + 1):
                value = int(input())
                row.append(value)  # Add values for edges to the current vertex (row).
            self.hypergraph.append(row)  # Add the completed row to the hypergraph.

    def print_hg(self):
        # Print the hypergraph in a readable format.
        print("Hypergraph:")
        for vertex in range(self.vertices):
            print("Vertex", vertex + 1, "edges:", end=" ")
            for edge in range(self.edges + 1):
                print(self.hypergraph[vertex][edge], end=" ")  # Print each edge value for the current vertex.
            print()  # Move to the next line for the next vertex.

    def sort(self):
        # Sort the hypergraph based on vertex degrees.
        for vertex in range(self.vertices):
            degree = 0
            for edge in range(1, self.edges + 1):
                degree += self.hypergraph[vertex][edge]  # Compute the degree of the vertex.
            print("Degree of vertex", vertex + 1, ":", degree)
            self.vertex_degrees.append(degree)  # Store the degree in the vertex_degrees list.

        # Sort the hypergraph vertices based on their degrees in non-increasing order.
        for i in range(self.vertices - 1):
            for j in range(i + 1, self.vertices):
                if self.vertex_degrees[i] < self.vertex_degrees[j]:
                    # Swap vertex degrees and corresponding hypergraph rows.
                    self.vertex_degrees[i], self.vertex_degrees[j] = self.vertex_degrees[j], self.vertex_degrees[i]
                    self.hypergraph[i], self.hypergraph[j] = self.hypergraph[j], self.hypergraph[i]

        self.sorted_status = True  # Set the sorted status to True.

    def dot_prod(self, v1, v2):
        # Compute the dot product of the specified vertices in the hypergraph.
        ans = 0
        for edge in range(1, self.edges):
            ans += self.hypergraph[v1][edge] * self.hypergraph[v2][edge]  # Compute dot product.
        return ans  # Return the computed dot product.

if __name__ == "__main__":
    v = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))

    # Create an instance of the Hypergraph class with the given number of vertices and edges.
    hg1 = Hypergraph(v, e)
    print("Original Hypergraph:")
    hg1.print_hg()  # Print the original hypergraph.
    hg1.sort()  # Sort the hypergraph based on vertex degrees.
    print("Sorted Hypergraph:")
    hg1.print_hg()  # Print the sorted hypergraph.

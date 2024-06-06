class Hypergraph:
    def __init__(self, v, e, vertex_names, edge_names, hg_matrix):
        self.vertices = v
        self.edges = e
        self.vertex_names_list = vertex_names
        self.edge_names_list = edge_names
        self.colors_used = 0
        self.sorted_status = False
        self.hypergraph_matrix = hg_matrix
        self.vertex_degrees = []
        self.colors_list = []
        self.vertex_indices = []

        for i in range(v):
            self.colors_list.append(-1)
            self.vertex_indices.append(i)

    def return_hypergraph_matrix(self):
        return self.hypergraph_matrix

    def return_vertex_names(self):
        return self.vertex_names_list

    def return_edge_names(self):
        return self.edge_names_list

    def return_colors_list(self):
        return self.colors_list

    def return_degrees_list(self):
        return self.vertex_degrees

    def return_entire_hypergraph(self):
        return self.vertices, self.edges, self.sorted_status, self.vertex_indices, self.vertex_names_list, self.vertex_names_list, self.edge_names_list, self.colors_list, self.hypergraph_matrix

    def return_if_sorted(self):
        return self.sorted_status

    def return_vertex_name(self, index):
        return self.vertex_names_list[index]

    def return_hypergraph_dataframe(self):
        df = pd.DataFrame()
        data = self.hypergraph_matrix
        df = pd.DataFrame(data, columns=self.edge_names_list, index=self.vertex_names_list)
        return df

    def return_degree_of_vertex(self, index):
        degree = 0
        for value in range(self.edges):
            if (self.hypergraph_matrix[index][value]):
                degree += 1
        return degree

    def store_degrees_of_all(self):
        for vertex in range(self.vertices):
            self.vertex_degrees.append(self.return_degree_of_vertex(vertex))





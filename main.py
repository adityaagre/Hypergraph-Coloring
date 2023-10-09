class Hypergraph:
    def __init__(self, v, e):
        self.vertices = v
        self.edges = e
        self.colors_used = 0
        self.sorted_status = False
        self.hypergraph = []
        self.hypergraph_sorted = []
        self.vertex_degrees = []
        self.vertex_colors = []
        for i in range (v):
            self.vertex_colors.append(-1) 

        for vertex in range(v):
            row = []
            print("Enter vertex", vertex)
            for edge in range(self.edges + 1):
                value = int(input())
                row.append(value)
            self.hypergraph.append(row)

    def print_hg(self):
        print("Hypergraph:")
        for vertex in range(self.vertices):
            print("Vertex", self.hypergraph[vertex][0], "edges:", end=" ")
            for edge in range(1, self.edges + 1):
                print(self.hypergraph[vertex][edge], end=" ")
            print()
        print("Colors in hypergraph")
        
        print(self.vertex_colors)

    def sort(self):
        for vertex in range(self.vertices):
            degree = 0
            for edge in range(1, self.edges + 1):
                degree += self.hypergraph[vertex][edge]
            print("Degree of vertex", vertex + 1, ":", degree)
            self.vertex_degrees.append(degree)

        for i in range(self.vertices - 1):
            for j in range(i + 1, self.vertices):
                if self.vertex_degrees[i] < self.vertex_degrees[j]:
                    self.vertex_degrees[i], self.vertex_degrees[j] = self.vertex_degrees[j], self.vertex_degrees[i]
                    self.hypergraph[i], self.hypergraph[j] = self.hypergraph[j], self.hypergraph[i]

        self.sorted_status = True

    def dot_prod(self, v1, v2):
        ans = 0
        for edge in range(1, self.edges):
            ans += self.hypergraph[v1][edge] * self.hypergraph[v2][edge]
        return ans

    
def proper_color(hg, colors):
    if(hg.sorted_status == False):
        hg.sort()

    for vertex_i in range(hg.vertices):
        #print(vertex_i)
        
        if(hg.vertex_colors[vertex_i] == -1):
            hg.colors_used += 1
            hg.vertex_colors[vertex_i] = hg.colors_used

            repeatable_list = []

            for vertex_j in range(vertex_i + 1, hg.vertices):
                if (hg.dot_prod(vertex_i, vertex_j) == 0):
                    repeatable_list.append(j)

            print(repeatable_list)
                    

                
            
            
       





##if __name__ == "__main__":
    
v = int(input("Enter number of vertices: "))

e = int(input("Enter number of edges: "))

hg1 = Hypergraph(v, e)
print("Original Hypergraph:")
hg1.print_hg()
hg1.sort()
print("Sorted Hypergraph:")
hg1.print_hg()

proper_color(hg1, [0,0])

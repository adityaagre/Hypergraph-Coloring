hypergraph.sort()
color = 0
current_color_list = []

for vertex in hypergraph:
    if vertex is uncolored:
        vertex.color(color)
        current_color_list.append(vertex)
        vertex_next = vertex

        while(vertex_next.next):
            vertex_next=vertex.next
            if vertex_next is not colored:
                if vertex_next is compatible(current_color_list):
                    vertex_next.color(color)
                    current_color_list.append(vertex_next)

                vertex_next = vertex_next.next
    if coloring.complete:
        return hg
    else:
        color++




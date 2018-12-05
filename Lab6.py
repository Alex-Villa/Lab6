import time
from Graph import *
from TopologicalSort import *
from Kruskal import *

def main():
    graph_set_up_start = time.clock()
    set_graph = Graph()

    vertex_A = Vertex('A')
    vertex_B = Vertex('B')
    vertex_C = Vertex('C')
    vertex_D = Vertex('D')
    vertex_E = Vertex('E')
    vertex_F = Vertex('F')
    vertex_G = Vertex('G')
    vertex_H = Vertex('H')
    vertex_I = Vertex('I')

    set_graph.add_vertex(vertex_A)
    set_graph.add_vertex(vertex_B)
    set_graph.add_vertex(vertex_C)
    set_graph.add_vertex(vertex_D)
    set_graph.add_vertex(vertex_E)
    set_graph.add_vertex(vertex_F)
    set_graph.add_vertex(vertex_G)
    set_graph.add_vertex(vertex_H)
    set_graph.add_vertex(vertex_I)

    set_graph.add_directed_edge(vertex_A, vertex_B)
    set_graph.add_directed_edge(vertex_A, vertex_C)
    set_graph.add_directed_edge(vertex_B, vertex_E)
    set_graph.add_directed_edge(vertex_B, vertex_C)
    set_graph.add_directed_edge(vertex_C, vertex_D)
    set_graph.add_directed_edge(vertex_C, vertex_F)
    set_graph.add_directed_edge(vertex_D, vertex_E)
    set_graph.add_directed_edge(vertex_D, vertex_F)
    set_graph.add_directed_edge(vertex_E, vertex_H)
    set_graph.add_directed_edge(vertex_E, vertex_G)
    set_graph.add_directed_edge(vertex_F, vertex_G)
    set_graph.add_directed_edge(vertex_G, vertex_H)
    set_graph.add_directed_edge(vertex_G, vertex_I)
    set_graph.add_directed_edge(vertex_H, vertex_I)

    kruskal_start = time.clock()
    print("*************** Kruskal's Algorithm from nodes *************** \n")

    set_graph2 = {'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], 'edges': set([
            (4, 'A', 'B'),
            (8, 'A', 'C'),
            (8, 'B', 'E'),
            (11, 'B', 'C'),
            (7, 'C', 'D'),
            (1, 'C', 'F'),
            (2, 'D', 'E'),
            (6, 'D', 'F'),
            (7, 'E', 'H'),
            (4, 'E', 'G'),
            (2, 'F', 'G'),
            (14, 'G', 'H'),
            (10, 'G', 'I'),
            (9, 'H', 'I'),
        ])
    }
    graph_set_up_end = time.clock()

    print("The graph has vertices: ", set_graph2['vertices'])
    print("This graph has a total of", len(set_graph2['edges']), "edges connecting the nodes")
    print("The graph set up took", graph_set_up_end - graph_set_up_start, "seconds\n")
    print("This is the minimal spanning tree has the following connections and weights:")
    kruskal(set_graph2)
    kruskal_end = time.clock()
    print("Kruskals algorithm took ", kruskal_end - kruskal_start, "seconds")

    topological_start = time.clock()
    print("\n*************** Topological Sort from nodes *************** \n")
    print("This is the Topological sort for the graph:")
    sorted_list = topological_sort(set_graph)
    first = True
    for vertex in sorted_list:
        if first:
            first = False
        else:
            print(', ', end='')
        print(vertex.label, end='')
    print("\n\n")
    topological_end = time.clock()
    print("Topological sort took ", topological_end - topological_start, "seconds")
main()
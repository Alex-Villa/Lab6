xroot = dict()
yroot = dict()


def create_set(vertex):
    xroot[vertex] = vertex
    yroot[vertex] = 0

def find(vertex):
    if xroot[vertex] is not vertex:
        xroot[vertex] = find(xroot[vertex])
    return xroot[vertex]

def union(vertex_a, vertex_b):
    root1 = find(vertex_a)
    root2 = find(vertex_b)
    if root1 is not root2:
        if yroot[root1] > yroot[root2]:
            xroot[root2] = root1
        else:
            xroot[root1] = root2
        if yroot[root1] is yroot[root2]:
            yroot[root2] += 1

def kruskal(graph):
    for vertex in graph['vertices']:
        create_set(vertex)
        mst = set()
        edges = list(graph['edges'])
        edges.sort()
    for edge in edges:
        weight, vertex_a, vertex_b = edge
        if find(vertex_a) is not find(vertex_b):
            union(vertex_a, vertex_b)
            mst.add(edge)
            print(edge)
    return sorted(mst)

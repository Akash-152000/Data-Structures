class Graph(object):
    def __init__(self,graph_dict=None):
        if graph_dict==None:
            graph_dict={}
        self.__graph_dict=graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())

    def generate_edges(self):
        edges=[]
        for vertex in self.__graph_dict:
            for connections in self.__graph_dict[vertex]:
                if {connections,vertex} not in edges:
                    edges.append((vertex,connections))
        return edges
    
    def add_vertex(self,vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex]=[]

    def add_edges(self,edge):
        edge=set(edge)
        (vertex1,vertex2)=tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1]=[vertex2]
         


graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }

g=Graph(graph)
print(g.vertices())
print(g.generate_edges())
g.add_vertex("g")
g.add_vertex("h")
print(g.vertices())
g.add_edges(("g","h"))
print(g.generate_edges())



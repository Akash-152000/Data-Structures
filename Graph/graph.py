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

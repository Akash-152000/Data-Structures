class Graph(object):
    def __init__(self,graph_dict=None):
        if graph_dict==None:
            graph_dict={}
        self.__graph_dict=graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())
    



graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }

g=Graph(graph)
print(g.vertices())

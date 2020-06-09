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


    def find_path(self,start,end,path=None):
        if path==None:
            path=[]
        graph=self.__graph_dict
        path=path+[start]
        if start==end:
            return path
        if start not in graph:
            return None
        for vertex in graph[start]:
            if vertex not in path:
                extended_path=self.find_path(vertex,end,path)
                if extended_path:
                    return extended_path
        return None
                    
    def find_all_path(self,start,end,path=[]):
        graph=self.__graph_dict
        path=path+[start]
        if start==end:
            return [path]
        if start not in graph:
            return []
        paths=[]
        for vertex in graph[start]:
            if vertex not in path:
                extended_path=self.find_all_path(vertex,end,path)

                for p in extended_path:
                    paths.append(p)
        return paths

    def degree(self,vertex):
        adj_vertices=self.__graph_dict[vertex]
        degree=len(adj_vertices)+ adj_vertices.count(vertex)
        return degree
        
    def find_isolated(self):
        isolated=[]
        graph=self.__graph_dict
        for vertex in graph:
            #print(isolated,vertex)
            if not graph[vertex]:
                isolated+=[vertex]
        return isolated

    def seq_degree(self):
        seq=[]
        graph=self.__graph_dict
        for vertex in graph:
            seq.append(self.degree(vertex))
        seq.sort(reverse=True)
        return tuple(seq)
                

graph = { "a" : ["d", "f"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : ["d"]
    }
g=Graph(graph)
print(g.vertices())
print(g.generate_edges())
g.add_vertex("g")
g.add_vertex("h")
print(g.vertices())
g.add_edges(("g","h"))
print(g.generate_edges())
print(g.find_path("a","a"))
print(g.find_all_path("a","b"))
print(g.degree("c"))
print(graph)
print(g.find_isolated())
print(g.seq_degree())

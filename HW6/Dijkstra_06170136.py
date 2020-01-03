from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        self.dict = defaultdict(list) 
        
    def addEdge(self,u,v,w):
        self.dict[w].append([u,v])
       
    def Dijkstra(self, s): 
        result = {}
        for i in range(self.V):
            last = self.graph[i]
            for j in range(len(last)):
                if last[j] != 0:
                    N_node = self.graph[j]
                    for n in range(len(N_node)):
                        if N_node[n] != 0:
                            if last[n] == 0 :
                                last[n] = last[j] + N_node[n]
                            elif last[n] > last[j] + N_node[n]:
                                last[n] = last[j] + N_node[n]
                            else:
                                pass
            result[str(i)] = self.graph[i][s]
        self.graph[i] = last

        return result
        
    def Kruskal(self):
        result = {}
        val = sorted(self.dict)
        check = [column for column in range(self.V)]  
        
        for i in val:
            for u,v in self.dict[i]:
                if check[u] == check[v]:
                    pass
                else:
                    check = [check[u]if x==check[v] else x for x in check]
                    result[str(u)+'-'+str(v)] = i
        return result

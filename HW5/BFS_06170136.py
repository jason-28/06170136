from collections import defaultdict 
  
class Graph:
  
    def __init__(self): 
        
        self.graph = defaultdict(list) 

     
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
     
    def BFS(self, s): 
       
        queue=[]
        visited=[]
        queue.append(s)
        visited.append(s)
    
        while queue:
            s=queue.pop(0)
            for i in self.graph[s]:
                if i in visited:
                    pass
                else:
                    visited.append(i)
                    queue.append(i)
        return visited
    
    def DFS(self, s):
        
        stack=[]
        visited=[]
        stack.append(s)
        
    
        while stack:
            s=stack.pop(-1)
            visited.append(s)
            for i in self.graph[s]:
                if i in visited:
                    pass
                else:
                    stack.append(i)
                        
        return visited

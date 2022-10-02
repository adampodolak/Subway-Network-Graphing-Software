import sys
sys.path.insert(0, '../GraphBuilder')
from GraphBuilder import EdgeGraph, BuildEdgeGraph

class Islands:
    
    def __init__(self, graph: EdgeGraph) -> None:
        self.graph = graph
    
    def dfs(self, temp_arr, station, marked):
        marked[station] = True

        temp_arr.append(station)

        for i in self.graph.edges:
            if i:
                for j in i.neighbours:
                    if marked[station] == False:
                        temp_arr = self.dfs(temp_arr, i, marked)
        return temp_arr

    def find_connected_components(self):
        marked = []
        connected_components = []
        for edge in range(len(self.graph.edges)):
            marked.append(False)
        for station in range(len(self.graph.edges)):
            if marked[station] == False:
                temp_arr = []
                connected_components.append(self.dfs(temp_arr, station, marked))
        return connected_components

graph = BuildEdgeGraph.build()

island_finder = Islands(graph)
connected_components = island_finder.find_connected_components()
print(connected_components)
from graph import *
from main import *

class itinerary:
    def __init__(self,graph) -> None:
        self.graph=graph
    
    def dikstras(self, s1,s2):
        #q holds priority list
        q = []
        distTo = []
        #qfollow and q indexes are connected. qfollow allows access to distTo[old node] 
        qfollow = []

        #initialize distTo array
        for i in range(len(self.graph.edges)):
            distTo.append(1000)
        distTo[s1-1] = 0

        #initialize q and qfollow
        q.append(self.graph.edges[s1-1])
        qfollow.append(q[0])
        q = self.find_neighbours(q,qfollow)


        #distTo[new node] = time to new node from old node + distTo[old node]
        while q:
            index = int(q[0].id)-1
            if distTo[index]>(int(q[0].time) + distTo[int(qfollow[0].id)-1]):
                distTo[index] = int(q[0].time) + distTo[int(qfollow[0].id)-1]
            q = self.find_neighbours(q,qfollow)
            q.pop(0)
            qfollow.pop(0)
        

        return distTo[s2-1]
            
    def find_neighbours(self, q,qfollow):
        for i in self.graph.edges[int(q[0].id)-1].neighbours:
            if i.marked == False:
                q.append(i)
                i.marked = True
                qfollow.append(q[0])
        return q

size = find_max('../_dataset/london.stations.csv')
graph = Edge(size)
graph.build_edgeGraph(format_data('../_dataset/london.connections.csv'),size)
sample = itinerary(graph)
print (sample.dikstras(76,286))

